from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config.settings import settings
from app.modules.api.v1.api import api_router
from app.middlewares.error_handler import error_handler_middleware
from app.utils.logger import get_logger
from app.utils.http_client import http_client
from app.db.mongodb import mongodb

from app.modules.api.v1.ml.service import ml_service

logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    
    # Connect to MongoDB
    try:
        await mongodb.connect_db(settings.MONGODB_URI, settings.DATABASE_NAME)
        logger.info("MongoDB connected successfully")
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {e}")

    # Pre-load ML model
    try:
        ml_service.load_model()
    except Exception as e:
        logger.error(f"Failed to pre-load ML model: {e}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down application...")
    await mongodb.close_db()
    await http_client.close()
    logger.info("Application shutdown complete")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Modern Python FastAPI Starter Project (Senior Level Architecture)",
    debug=settings.DEBUG,
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom error handling
app.middleware("http")(error_handler_middleware)

# Register aggregated router
app.include_router(api_router, prefix=settings.API_V1_PREFIX)

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}!",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "api": {
            "v1": settings.API_V1_PREFIX
        }
    }

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting server on {settings.HOST}:{settings.PORT}")
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )
