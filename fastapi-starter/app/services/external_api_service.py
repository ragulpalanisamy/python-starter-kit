"""
External API Service

This module contains business logic for integrating with external APIs:
- JSONPlaceholder (fake REST API)
- Open-Meteo (weather data)

The service layer separates business logic from route handlers,
making the code more maintainable and testable.
"""

from typing import List, Dict, Any
from app.config import settings
from app.helpers.http_client import http_client
from app.helpers.logger import get_logger

logger = get_logger(__name__)


class ExternalAPIService:
    """
    Service class for external API integrations.
    
    This class encapsulates all logic for calling external APIs
    and returning raw data as dictionaries.
    """
    
    # JSONPlaceholder API methods
    async def get_posts(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Fetch blog posts from JSONPlaceholder API.
        
        JSONPlaceholder is a free fake REST API for testing and prototyping.
        It provides realistic-looking data without requiring authentication.
        
        Args:
            limit: Maximum number of posts to return (default: 10)
        
        Returns:
            List[Post]: List of blog post objects
        
        Example:
            >>> service = ExternalAPIService()
            >>> posts = await service.get_posts(limit=5)
            >>> print(posts[0].title)
        """
        try:
            url = f"{settings.JSONPLACEHOLDER_URL}/posts"
            logger.info(f"Fetching posts from JSONPlaceholder (limit: {limit})")
            
            # Make the HTTP request
            data = await http_client.get(url)
            
            # Return the raw data
            posts = data[:limit]
            
            logger.info(f"Successfully fetched {len(posts)} posts")
            return posts
        
        except Exception as e:
            logger.error(f"Error fetching posts: {e}")
            raise
    
    async def get_post_by_id(self, post_id: int) -> Dict[str, Any]:
        """
        Fetch a single post by ID from JSONPlaceholder API.
        
        Args:
            post_id: ID of the post to fetch
        
        Returns:
            Post: Single post object
        
        Raises:
            Exception: If post not found or API error occurs
        """
        try:
            url = f"{settings.JSONPLACEHOLDER_URL}/posts/{post_id}"
            logger.info(f"Fetching post {post_id}")
            
            data = await http_client.get(url)
            
            logger.info(f"Successfully fetched post {post_id}")
            return data
        
        except Exception as e:
            logger.error(f"Error fetching post {post_id}: {e}")
            raise
    
    async def get_users(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Fetch users from JSONPlaceholder API.
        
        Args:
            limit: Maximum number of users to return (default: 10)
        
        Returns:
            List[User]: List of user objects
        """
        try:
            url = f"{settings.JSONPLACEHOLDER_URL}/users"
            logger.info(f"Fetching users from JSONPlaceholder (limit: {limit})")
            
            data = await http_client.get(url)
            users = data[:limit]
            
            logger.info(f"Successfully fetched {len(users)} users")
            return users
        
        except Exception as e:
            logger.error(f"Error fetching users: {e}")
            raise
    
    # Open-Meteo API methods
    async def get_weather(self, latitude: float, longitude: float) -> Dict[str, Any]:
        """
        Fetch current weather data from Open-Meteo API.
        
        Open-Meteo is a free weather API that doesn't require authentication.
        It provides accurate weather data for any location worldwide.
        
        Args:
            latitude: Latitude coordinate (-90 to 90)
            longitude: Longitude coordinate (-180 to 180)
        
        Returns:
            WeatherResponse: Weather data for the specified location
        
        Example:
            >>> service = ExternalAPIService()
            >>> # Get weather for Chennai, India
            >>> weather = await service.get_weather(13.0827, 80.2707)
            >>> print(f"Temperature: {weather.temperature}°C")
        """
        try:
            url = f"{settings.OPEN_METEO_URL}/forecast"
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "current_weather": "true"
            }
            
            logger.info(f"Fetching weather for ({latitude}, {longitude})")
            
            data = await http_client.get(url, params=params)
            
            # Extract current weather data from the response
            current = data.get("current_weather", {})
            
            # Return formatted weather data
            weather = {
                "latitude": latitude,
                "longitude": longitude,
                "temperature": current.get("temperature", 0),
                "windspeed": current.get("windspeed", 0),
                "weather_description": self._get_weather_description(
                    current.get("weathercode", 0)
                )
            }
            
            logger.info(f"Successfully fetched weather data")
            return weather
        
        except Exception as e:
            logger.error(f"Error fetching weather: {e}")
            raise
    
    def _get_weather_description(self, code: int) -> str:
        """
        Convert weather code to human-readable description.
        
        Open-Meteo uses WMO weather codes.
        
        Args:
            code: WMO weather code
        
        Returns:
            str: Human-readable weather description
        """
        # Simplified weather code mapping
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Depositing rime fog",
            51: "Light drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            80: "Slight rain showers",
            95: "Thunderstorm"
        }
        return weather_codes.get(code, "Unknown")


# Global service instance - import this in route handlers
external_api_service = ExternalAPIService()
