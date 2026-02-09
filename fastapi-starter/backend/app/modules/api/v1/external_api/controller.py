"""
External API Controller

Handles requests for external API integration.
Calls services to fetch data from external APIs.

Similar to Express.js controllers - handles request/response.
"""

from fastapi import HTTPException, status
from typing import List
from . import service as external_api_service


async def get_posts(limit: int = 10):
    """
    Get blog posts from JSONPlaceholder API.
    
    Args:
        limit: Number of posts to return
    
    Returns:
        list: List of blog posts
    """
    try:
        posts = await external_api_service.get_posts(limit=limit)
        return posts
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to fetch posts: {str(e)}"
        )


async def get_post_by_id(post_id: int):
    """
    Get a specific post by ID.
    
    Args:
        post_id: ID of the post to fetch
    
    Returns:
        dict: Single post data
    """
    try:
        post = await external_api_service.get_post_by_id(post_id)
        return post
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {post_id} not found: {str(e)}"
        )


async def get_users(limit: int = 10):
    """
    Get users from JSONPlaceholder API.
    
    Args:
        limit: Number of users to return
    
    Returns:
        list: List of users
    """
    try:
        users = await external_api_service.get_users(limit=limit)
        return users
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to fetch users: {str(e)}"
        )


async def get_weather(latitude: float, longitude: float):
    """
    Get weather data for coordinates.
    
    Args:
        latitude: Latitude coordinate
        longitude: Longitude coordinate
    
    Returns:
        dict: Weather data
    """
    try:
        weather = await external_api_service.get_weather(latitude, longitude)
        return weather
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to fetch weather: {str(e)}"
        )
