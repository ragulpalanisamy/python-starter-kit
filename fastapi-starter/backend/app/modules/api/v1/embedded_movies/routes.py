from fastapi import APIRouter, Depends, Query
from app.db.mongodb import get_mongodb
from app.modules.api.v1.embedded_movies.service import EmbeddedMovieService
from app.modules.api.v1.embedded_movies.controller import EmbeddedMovieController
from app.validations.pagination import PaginatedResponse
from app.Models.domain_models import EmbeddedMovieModel
from app.validations.embedded_movie_schema import EmbeddedMovieCreate

router = APIRouter()

async def get_embedded_movie_controller(mongodb = Depends(get_mongodb)):
    service = EmbeddedMovieService(mongodb)
    return EmbeddedMovieController(service)

@router.get("/", response_model=PaginatedResponse[EmbeddedMovieModel])
async def get_movies(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    controller: EmbeddedMovieController = Depends(get_embedded_movie_controller)
):
    """Get paginated embedded movies."""
    return await controller.list_movies(page, page_size)

@router.get("/{movie_id}", response_model=EmbeddedMovieModel)
async def get_movie(
    movie_id: str,
    controller: EmbeddedMovieController = Depends(get_embedded_movie_controller)
):
    """Get a single embedded movie by ID."""
    return await controller.get_movie(movie_id)

@router.post("/", response_model=EmbeddedMovieModel)
async def create_movie(
    movie_data: EmbeddedMovieCreate,
    controller: EmbeddedMovieController = Depends(get_embedded_movie_controller)
):
    """Create a new embedded movie."""
    return await controller.create_movie(movie_data)
