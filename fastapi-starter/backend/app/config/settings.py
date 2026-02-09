"""
Configuration Management

This module handles all application configuration using Pydantic Settings.
It loads configuration from environment variables and provides type-safe access.

Usage:
    from app.config.settings import settings
    print(settings.APP_NAME)
"""

from pydantic_settings import BaseSettings
from functools import lru_cache
import os

from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    Pydantic automatically loads values from:
    1. Environment variables
    2. .env file (if present)
    3. Default values defined here
    """
    
    # Application settings
    APP_NAME: str = "FastAPI Starter"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True
    
    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # API settings
    API_V1_PREFIX: str = "/api/v1"
    
    # External API URLs (no authentication required)
    JSONPLACEHOLDER_URL: str = "https://jsonplaceholder.typicode.com"
    OPEN_METEO_URL: str = "https://api.open-meteo.com/v1"
    
    # HTTP client settings
    REQUEST_TIMEOUT: int = 30  # seconds
    
    # MongoDB settings
    MONGODB_URI: str
    DATABASE_NAME: str = "sample_mflix"
    
    # ML settings
    ENABLE_ML: bool = True
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        """Pydantic configuration"""
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.
    
    Using @lru_cache ensures we only create one Settings instance
    and reuse it throughout the application (singleton pattern).
    
    Returns:
        Settings: Application settings instance
    """
    return Settings()


# Global settings instance - import this in other modules
settings = get_settings()
