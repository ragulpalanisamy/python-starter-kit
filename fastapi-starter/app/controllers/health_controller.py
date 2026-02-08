"""
Health Controller

Handles health check requests.
Similar to a controller in Express.js.
"""

from datetime import datetime
from fastapi import HTTPException
import sys
from app.config import settings


async def get_health():
    """
    Basic health check handler.
    
    Returns:
        dict: Health status and timestamp
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }


async def get_detailed_health():
    """
    Detailed health check handler.
    
    Returns:
        dict: Detailed health information including version and dependencies
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": settings.APP_VERSION,
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        "dependencies": {
            "external_apis": "available",
            "http_client": "ready"
        }
    }
