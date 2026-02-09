from fastapi import APIRouter, Depends, Query
from app.db.mongodb import get_mongodb
from app.modules.api.v1.movies.service import MovieService
from app.modules.api.v1.movies.controller import MovieController
from app.validations.pagination import PaginatedResponse
from app.Models.domain_models import MovieModel
from app.validations.movie_schema import MovieCreate, MovieUpdate

router = APIRouter()

async def get_movie_controller(mongodb = Depends(get_mongodb)):
    service = MovieService(mongodb)
    return MovieController(service)

@router.get("/", response_model=PaginatedResponse[MovieModel])
async def get_movies(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    controller: MovieController = Depends(get_movie_controller)
):
    """Get paginated movies."""
    return await controller.list_movies(page, page_size)

@router.get("/{movie_id}", response_model=MovieModel)
async def get_movie(
    movie_id: str,
    controller: MovieController = Depends(get_movie_controller)
):
    """Get a single movie by ID."""
    return await controller.get_movie(movie_id)

@router.post("/", response_model=MovieModel)
async def create_movie(
    movie_data: MovieCreate,
    controller: MovieController = Depends(get_movie_controller)
):
    """Create a new movie."""
    return await controller.create_movie(movie_data)

@router.put("/{movie_id}", response_model=MovieModel)
async def update_movie(
    movie_id: str,
    movie_data: MovieUpdate,
    controller: MovieController = Depends(get_movie_controller)
):
    """Update a movie."""
    return await controller.update_movie(movie_id, movie_data)

@router.delete("/{movie_id}")
async def delete_movie(
    movie_id: str,
    controller: MovieController = Depends(get_movie_controller)
):
    """Delete a movie."""
    return await controller.delete_movie(movie_id)
