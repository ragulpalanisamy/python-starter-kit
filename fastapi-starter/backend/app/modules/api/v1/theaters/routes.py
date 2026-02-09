from fastapi import APIRouter, Depends, Query
from app.db.mongodb import get_mongodb
from app.modules.api.v1.theaters.service import TheaterService
from app.modules.api.v1.theaters.controller import TheaterController
from app.validations.pagination import PaginatedResponse
from app.Models.domain_models import TheaterModel
from app.validations.theater_schema import TheaterCreate, TheaterUpdate

router = APIRouter()

async def get_theater_controller(mongodb = Depends(get_mongodb)):
    service = TheaterService(mongodb)
    return TheaterController(service)

@router.get("/", response_model=PaginatedResponse[TheaterModel])
async def get_theaters(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    controller: TheaterController = Depends(get_theater_controller)
):
    """Get paginated theaters."""
    return await controller.list_theaters(page, page_size)

@router.get("/{theater_id}", response_model=TheaterModel)
async def get_theater(
    theater_id: str,
    controller: TheaterController = Depends(get_theater_controller)
):
    """Get a single theater by ID."""
    return await controller.get_theater(theater_id)

@router.post("/", response_model=TheaterModel)
async def create_theater(
    theater_data: TheaterCreate,
    controller: TheaterController = Depends(get_theater_controller)
):
    """Create a new theater."""
    return await controller.create_theater(theater_data)

@router.put("/{theater_id}", response_model=TheaterModel)
async def update_theater(
    theater_id: str,
    theater_data: TheaterUpdate,
    controller: TheaterController = Depends(get_theater_controller)
):
    """Update a theater."""
    return await controller.update_theater(theater_id, theater_data)

@router.delete("/{theater_id}")
async def delete_theater(
    theater_id: str,
    controller: TheaterController = Depends(get_theater_controller)
):
    """Delete a theater."""
    return await controller.delete_theater(theater_id)
