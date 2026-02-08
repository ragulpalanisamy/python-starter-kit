"""
Health Routes

Defines health check endpoints.
Similar to Express.js route files.

Pattern: Route → Controller → Service (if needed)
"""

from fastapi import APIRouter
from app.controllers import health_controller

# Create router (like Express Router)
router = APIRouter(
    prefix="/health",
    tags=["Health"],  # Groups endpoints in API docs
)


@router.get(
    "",
    summary="Basic Health Check",
    description="Returns basic health status of the API"
)
async def health_check():
    """
    Basic health check endpoint.
    
    Route calls controller, which returns health status.
    """
    return await health_controller.get_health()


@router.get(
    "/detailed",
    summary="Detailed Health Check",
    description="Returns detailed health status including system information"
)
async def detailed_health_check():
    """
    Detailed health check endpoint.
    
    Route calls controller for detailed system info.
    """
    return await health_controller.get_detailed_health()
