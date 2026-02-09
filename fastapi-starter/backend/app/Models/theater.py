from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from app.Models.base import PyObjectId, MongoBaseModel

class TheaterLocation(BaseModel):
    """Theater location details."""
    address: Dict[str, str]
    geo: Dict[str, Any]

class TheaterModel(BaseModel):
    """Model for MFlix Theater documents."""
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    theaterId: int = Field(..., description="Unique theater identifier")
    location: TheaterLocation

    class Config(MongoBaseModel):
        pass
