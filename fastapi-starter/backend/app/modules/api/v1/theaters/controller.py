import math
from fastapi import HTTPException
from app.modules.api.v1.theaters.service import TheaterService
from app.validations.pagination import PaginatedResponse
from app.validations.theater_schema import TheaterCreate, TheaterUpdate
from app.Models.domain_models import TheaterModel
from app.utils.logger import get_logger

logger = get_logger(__name__)

class TheaterController:
    """Controller for Theater endpoints."""
    
    def __init__(self, theater_service: TheaterService):
        self.theater_service = theater_service

    async def list_theaters(self, page: int, page_size: int) -> PaginatedResponse[TheaterModel]:
        """List theaters with pagination."""
        try:
            theaters, total = await self.theater_service.get_theaters(page, page_size)
            total_pages = math.ceil(total / page_size) if total > 0 else 0
            return PaginatedResponse(
                items=theaters,
                total=total,
                page=page,
                page_size=page_size,
                total_pages=total_pages,
                has_next=page < total_pages,
                has_prev=page > 1
            )
        except Exception as e:
            logger.error(f"Error listing theaters: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch theaters")

    async def get_theater(self, theater_id: str) -> TheaterModel:
        """Get a theater by ID."""
        theater = await self.theater_service.get_theater(theater_id)
        if not theater:
            raise HTTPException(status_code=404, detail="Theater not found")
        return theater

    async def create_theater(self, theater_data: TheaterCreate) -> TheaterModel:
        """Create a new theater."""
        try:
            db_theater = TheaterModel(**theater_data.dict())
            return await self.theater_service.create_theater(db_theater)
        except Exception as e:
            logger.error(f"Error creating theater: {e}")
            raise HTTPException(status_code=500, detail="Failed to create theater")

    async def update_theater(self, theater_id: str, theater_data: TheaterUpdate) -> TheaterModel:
        """Update a theater."""
        try:
            update_dict = {k: v for k, v in theater_data.dict().items() if v is not None}
            theater = await self.theater_service.update_theater(theater_id, update_dict)
            if not theater:
                raise HTTPException(status_code=404, detail="Theater not found")
            return theater
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error updating theater: {e}")
            raise HTTPException(status_code=500, detail="Failed to update theater")

    async def delete_theater(self, theater_id: str) -> dict:
        """Delete a theater."""
        try:
            success = await self.theater_service.delete_theater(theater_id)
            if not success:
                raise HTTPException(status_code=404, detail="Theater not found")
            return {"message": "Theater deleted successfully"}
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error deleting theater: {e}")
            raise HTTPException(status_code=500, detail="Failed to delete theater")
