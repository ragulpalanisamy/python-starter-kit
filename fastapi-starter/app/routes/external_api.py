"""
External API Routes

Defines endpoints for external API integration.
Similar to Express.js route files.

Pattern: Route → Controller → Service → External API
"""

from fastapi import APIRouter, Query, Path
from app.controllers import external_controller
from pydantic import BaseModel, Field

# Create router
router = APIRouter(
    prefix="/external",
    tags=["External APIs"],
)


# Request/Response models (inline, not in separate models folder)
class WeatherRequest(BaseModel):
    """Weather request model"""
    latitude: float = Field(..., ge=-90, le=90, description="Latitude coordinate")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude coordinate")


# JSONPlaceholder endpoints
@router.get(
    "/posts",
    summary="Get Blog Posts",
    description="Fetch blog posts from JSONPlaceholder (fake REST API)"
)
async def get_posts(
    limit: int = Query(default=10, ge=1, le=100, description="Number of posts to return")
):
    """Get blog posts - Route → Controller → Service"""
    return await external_controller.get_posts(limit=limit)


@router.get(
    "/posts/{post_id}",
    summary="Get Post by ID",
    description="Fetch a specific blog post by ID"
)
async def get_post_by_id(
    post_id: int = Path(..., ge=1, description="ID of the post to fetch")
):
    """Get single post - Route → Controller → Service"""
    return await external_controller.get_post_by_id(post_id)


@router.get(
    "/users",
    summary="Get Users",
    description="Fetch users from JSONPlaceholder"
)
async def get_users(
    limit: int = Query(default=10, ge=1, le=100, description="Number of users to return")
):
    """Get users - Route → Controller → Service"""
    return await external_controller.get_users(limit=limit)


# Open-Meteo (Weather) endpoints
@router.post(
    "/weather",
    summary="Get Weather Data",
    description="Get current weather data for specified coordinates"
)
async def get_weather(request: WeatherRequest):
    """Get weather - Route → Controller → Service → Open-Meteo API"""
    return await external_controller.get_weather(
        latitude=request.latitude,
        longitude=request.longitude
    )
