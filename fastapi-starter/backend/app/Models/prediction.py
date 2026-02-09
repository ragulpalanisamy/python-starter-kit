from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.Models.base import PyObjectId, MongoBaseModel

class PredictionModel(BaseModel):
    """Model for ML prediction documents."""
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    prediction_id: str = Field(..., description="Unique prediction identifier")
    text: str = Field(..., description="Input text")
    sentiment: str = Field(..., description="Predicted sentiment")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    model_version: str = Field(..., description="Model version")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    batch_id: Optional[str] = None
    processing_time_ms: Optional[float] = None
    
    class Config(MongoBaseModel):
        pass
