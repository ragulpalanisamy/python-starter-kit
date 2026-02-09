from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000, description="Text to analyze")

class BatchPredictRequest(BaseModel):
    texts: List[str] = Field(..., min_items=1, max_items=100, description="List of texts")

class PredictionResponse(BaseModel):
    prediction_id: str
    text: str
    sentiment: str
    confidence: float
    model_version: str
    processing_time_ms: float
    created_at: datetime
