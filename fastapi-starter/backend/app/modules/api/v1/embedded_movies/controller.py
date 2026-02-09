import math
from fastapi import HTTPException
from app.modules.api.v1.embedded_movies.service import EmbeddedMovieService
from app.validations.pagination import PaginatedResponse
from app.validations.embedded_movie_schema import EmbeddedMovieCreate
from app.Models.domain_models import EmbeddedMovieModel
from app.utils.logger import get_logger

logger = get_logger(__name__)

class EmbeddedMovieController:
    """Controller for Embedded Movie endpoints."""
    
    def __init__(self, movie_service: EmbeddedMovieService):
        self.movie_service = movie_service

    async def list_movies(self, page: int, page_size: int) -> PaginatedResponse[EmbeddedMovieModel]:
        """List embedded movies with pagination."""
        try:
            movies, total = await self.movie_service.get_movies(page, page_size)
            total_pages = math.ceil(total / page_size) if total > 0 else 0
            return PaginatedResponse(
                items=movies,
                total=total,
                page=page,
                page_size=page_size,
                total_pages=total_pages,
                has_next=page < total_pages,
                has_prev=page > 1
            )
        except Exception as e:
            logger.error(f"Error listing embedded movies: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch embedded movies")

    async def get_movie(self, movie_id: str) -> EmbeddedMovieModel:
        """Get an embedded movie by ID."""
        movie = await self.movie_service.get_movie(movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Embedded movie not found")
        return movie

    async def create_movie(self, movie_data: EmbeddedMovieCreate) -> EmbeddedMovieModel:
        """Create a new embedded movie."""
        try:
            db_movie = EmbeddedMovieModel(**movie_data.dict())
            return await self.movie_service.create_movie(db_movie)
        except Exception as e:
            logger.error(f"Error creating embedded movie: {e}")
            raise HTTPException(status_code=500, detail="Failed to create embedded movie")
