"""
Global Error Handler Middleware

This middleware catches all unhandled exceptions and returns
consistent error responses to the client.

It ensures that:
- All errors are logged
- Clients receive user-friendly error messages
- Internal errors don't expose sensitive information
"""

from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.utils.logger import get_logger

logger = get_logger(__name__)


async def error_handler_middleware(request: Request, call_next):
    """
    Middleware to handle all unhandled exceptions.
    
    This catches any exception that occurs during request processing
    and returns a consistent JSON error response.
    
    Args:
        request: The incoming request
        call_next: The next middleware or route handler
    
    Returns:
        Response: Either the normal response or an error response
    """
    try:
        # Process the request
        response = await call_next(request)
        return response
    
    except Exception as e:
        # Log the error with full details
        logger.error(
            f"Unhandled exception: {str(e)}",
            exc_info=True,
            extra={
                "path": request.url.path,
                "method": request.method,
                "client": request.client.host if request.client else "unknown"
            }
        )
        
        # Return a user-friendly error response
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error": "Internal Server Error",
                "message": "An unexpected error occurred. Please try again later.",
                "path": request.url.path
            }
        )
