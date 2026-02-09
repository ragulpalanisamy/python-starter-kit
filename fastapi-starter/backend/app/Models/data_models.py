from typing import Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field
from app.Models.base import PyObjectId, MongoBaseModel

class DataUploadModel(BaseModel):
    """Model for data upload documents."""
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    upload_id: str = Field(..., description="Unique upload identifier")
    filename: str = Field(..., description="Original filename")
    file_type: str = Field(..., description="File type (csv, json, parquet)")
    size: int = Field(..., description="File size in bytes")
    upload_date: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="pending", description="Processing status")
    user_id: Optional[str] = None
    error_message: Optional[str] = None
    
    class Config(MongoBaseModel):
        pass

class ProcessedDataModel(BaseModel):
    """Model for processed data documents."""
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    process_id: str = Field(..., description="Unique process identifier")
    upload_id: str = Field(..., description="Reference to upload")
    data: Optional[Dict[str, Any]] = Field(default=None, description="Processed data")
    stats: Dict[str, Any] = Field(..., description="Data statistics")
    process_date: datetime = Field(default_factory=datetime.utcnow)
    processing_time: Optional[float] = Field(None, description="Processing time in seconds")
    
    class Config(MongoBaseModel):
        pass
