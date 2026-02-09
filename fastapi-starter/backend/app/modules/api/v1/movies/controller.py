import math
from fastapi import HTTPException
from app.modules.api.v1.movies.service import MovieService
from app.validations.pagination import PaginatedResponse
from app.validations.movie_schema import MovieCreate, MovieUpdate
from app.Models.domain_models import MovieModel
from app.utils.logger import get_logger

logger = get_logger(__name__)

class MovieController:
    """Controller for Movie endpoints."""
    
    def __init__(self, movie_service: MovieService):
        self.movie_service = movie_service

    async def list_movies(self, page: int, page_size: int) -> PaginatedResponse[MovieModel]:
        """List movies with pagination."""
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
            logger.error(f"Error listing movies: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch movies")

    async def get_movie(self, movie_id: str) -> MovieModel:
        """Get a movie by ID."""
        movie = await self.movie_service.get_movie(movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie

    async def create_movie(self, movie_data: MovieCreate) -> MovieModel:
        """Create a new movie."""
        try:
            # Convert schema to domain model for service
            db_movie = MovieModel(**movie_data.dict())
            return await self.movie_service.create_movie(db_movie)
        except Exception as e:
            logger.error(f"Error creating movie: {e}")
            raise HTTPException(status_code=500, detail="Failed to create movie")

    async def update_movie(self, movie_id: str, movie_data: MovieUpdate) -> MovieModel:
        """Update a movie."""
        try:
            # Filter out None values to only update provided fields
            update_dict = {k: v for k, v in movie_data.dict().items() if v is not None}
            movie = await self.movie_service.update_movie(movie_id, update_dict)
            if not movie:
                raise HTTPException(status_code=404, detail="Movie not found")
            return movie
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error updating movie: {e}")
            raise HTTPException(status_code=500, detail="Failed to update movie")

    async def delete_movie(self, movie_id: str) -> dict:
        """Delete a movie."""
        try:
            success = await self.movie_service.delete_movie(movie_id)
            if not success:
                raise HTTPException(status_code=404, detail="Movie not found")
            return {"message": "Movie deleted successfully"}
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error deleting movie: {e}")
            raise HTTPException(status_code=500, detail="Failed to delete movie")
