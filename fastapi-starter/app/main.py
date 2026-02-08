"""
FastAPI Starter - Main Application

This is the main entry point for the FastAPI application.
It sets up the FastAPI app, registers routers, configures middleware,
and handles application lifecycle events.

To run this application:
    uvicorn app.main:app --reload

The application will be available at:
    - API: http://localhost:8000
    - Swagger UI (API docs): http://localhost:8000/docs
    - ReDoc (alternative docs): http://localhost:8000/redoc
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.routes import health, external_api
from app.middleware.error_handler import error_handler_middleware
from app.helpers.logger import get_logger
from app.helpers.http_client import http_client

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.
    
    This function handles startup and shutdown events for the application.
    It's called when the application starts and when it shuts down.
    
    Startup tasks:
        - Log application start
        - Initialize resources (if needed)
    
    Shutdown tasks:
        - Close HTTP client connections
        - Cleanup resources
    """
    # Startup
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    logger.info(f"Debug mode: {settings.DEBUG}")
    logger.info("Application startup complete")
    
    yield  # Application runs here
    
    # Shutdown
    logger.info("Shutting down application...")
    await http_client.close()  # Close HTTP client connections
    logger.info("Application shutdown complete")


# Create FastAPI application instance
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="""
    ## Modern Python FastAPI Starter Project
    
    This is a production-ready FastAPI project demonstrating:
    - **FastAPI framework** for building REST APIs
    - **External API integration** (JSONPlaceholder, Open-Meteo)
    - **Async/await** for non-blocking I/O
    - **Pydantic** for data validation
    - **Structured logging** throughout
    
    ## 📚 API Endpoints
    
    ### Health Checks
    - `GET /health` - Basic health check
    - `GET /health/detailed` - Detailed system information
    
    ### External APIs
    - **JSONPlaceholder**: Fake REST API for testing
      - `GET /api/v1/external/posts` - Get blog posts
      - `GET /api/v1/external/posts/{id}` - Get specific post
      - `GET /api/v1/external/users` - Get users
    - **Open-Meteo**: Free weather API
      - `POST /api/v1/external/weather` - Get weather data
    
    ### Getting Started
    
    1. Install dependencies: `uv sync`
    2. Run the server: `uv run uvicorn app.main:app --reload`
    3. Visit the docs: http://localhost:8000/docs
    """,
    debug=settings.DEBUG,
    lifespan=lifespan,  # Register lifespan manager
)


# Configure CORS (Cross-Origin Resource Sharing)
# This allows your API to be called from web browsers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Add custom error handling middleware
# This must be added after CORS middleware
app.middleware("http")(error_handler_middleware)


# Register routers
# Each router handles a specific feature area of the API

# Health check endpoints (no prefix, available at /health)
app.include_router(health.router)

# API v1 endpoints (all under /api/v1)
app.include_router(
    external_api.router,
    prefix=settings.API_V1_PREFIX,
)


# Root endpoint
@app.get(
    "/",
    tags=["Root"],
    summary="Root Endpoint",
    description="Welcome message and API information"
)
async def root():
    """
    Root endpoint of the API.
    
    This provides basic information about the API and links to documentation.
    
    Returns:
        dict: Welcome message and API information
    """
    return {
        "message": f"Welcome to {settings.APP_NAME}!",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/health",
        "api": {
            "external_apis": f"{settings.API_V1_PREFIX}/external"
        }
    }


# This allows running the app directly with: python -m app.main
if __name__ == "__main__":
    import uvicorn
    
    logger.info(f"Starting server on {settings.HOST}:{settings.PORT}")
    
    # Run the application
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,  # Auto-reload on code changes in debug mode
        log_level=settings.LOG_LEVEL.lower()
    )
