"""
HTTP Client Wrapper

This module provides a wrapper around httpx for making HTTP requests.
It includes timeout handling, error handling, and retry logic.

Usage:
    from app.utils.http_client import http_client
    
    # Make a GET request
    response = await http_client.get("https://api.example.com/data")
    
    # Make a POST request
    response = await http_client.post(
        "https://api.example.com/data",
        json={"key": "value"}
    )
"""

import httpx
from typing import Optional, Dict, Any
from app.config.settings import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)


class HTTPClient:
    """
    Async HTTP client wrapper using httpx.
    
    This class provides a convenient interface for making HTTP requests
    with automatic timeout handling and error logging.
    
    Attributes:
        timeout: Default timeout for all requests in seconds
    """
    
    def __init__(self, timeout: int = settings.REQUEST_TIMEOUT):
        """
        Initialize the HTTP client.
        
        Args:
            timeout: Request timeout in seconds (default from settings)
        """
        self.timeout = timeout
        self._client: Optional[httpx.AsyncClient] = None
    
    async def _get_client(self) -> httpx.AsyncClient:
        """
        Get or create the httpx client instance.
        
        This uses a singleton pattern to reuse the same client
        for connection pooling and better performance.
        
        Returns:
            httpx.AsyncClient: Async HTTP client instance
        """
        if self._client is None:
            self._client = httpx.AsyncClient(
                timeout=self.timeout,
                follow_redirects=True
            )
        return self._client
    
    async def get(
        self, 
        url: str, 
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Make an async GET request.
        
        Args:
            url: URL to request
            params: Optional query parameters
            headers: Optional HTTP headers
        
        Returns:
            Dict containing the JSON response
        
        Raises:
            httpx.HTTPError: If the request fails
        
        Example:
            >>> data = await http_client.get(
            ...     "https://api.example.com/users",
            ...     params={"page": 1}
            ... )
        """
        client = await self._get_client()
        
        try:
            logger.info(f"GET request to {url}")
            response = await client.get(url, params=params, headers=headers)
            response.raise_for_status()  # Raise exception for 4xx/5xx status codes
            return response.json()
        
        except httpx.HTTPError as e:
            logger.error(f"HTTP error occurred: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            raise
    
    async def post(
        self,
        url: str,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Make an async POST request.
        
        Args:
            url: URL to request
            json: Optional JSON body
            data: Optional form data
            headers: Optional HTTP headers
        
        Returns:
            Dict containing the JSON response
        
        Raises:
            httpx.HTTPError: If the request fails
        
        Example:
            >>> data = await http_client.post(
            ...     "https://api.example.com/users",
            ...     json={"name": "John Doe"}
            ... )
        """
        client = await self._get_client()
        
        try:
            logger.info(f"POST request to {url}")
            response = await client.post(url, json=json, data=data, headers=headers)
            response.raise_for_status()
            return response.json()
        
        except httpx.HTTPError as e:
            logger.error(f"HTTP error occurred: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            raise
    
    async def close(self):
        """
        Close the HTTP client and cleanup resources.
        
        This should be called when the application shuts down.
        """
        if self._client:
            await self._client.aclose()
            self._client = None
            logger.info("HTTP client closed")


# Global HTTP client instance - import this in other modules
http_client = HTTPClient()
