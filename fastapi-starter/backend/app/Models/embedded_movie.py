from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field
from app.Models.base import PyObjectId, MongoBaseModel

class PlotEmbedding(BaseModel):
    """Plot embedding details."""
    binary: Dict[str, Any] = Field(..., alias="$binary")

class EmbeddedMovieModel(BaseModel):
    """Model for MFlix Embedded Movie documents."""
    
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(..., description="The title of the movie")
    year: int = Field(..., description="Release year")
    plot: Optional[str] = Field(None, description="Short summary of the plot")
    fullplot: Optional[str] = Field(None, description="Detailed plot description")
    genres: List[str] = Field(default_factory=list)
    runtime: Optional[int] = Field(None, description="Runtime in minutes")
    cast: List[str] = Field(default_factory=list)
    languages: List[str] = Field(default_factory=list)
    released: Optional[datetime] = None
    directors: List[str] = Field(default_factory=list)
    writers: List[str] = Field(default_factory=list)
    countries: List[str] = Field(default_factory=list)
    awards: Dict[str, Any] = Field(default_factory=dict)
    imdb: Dict[str, Any] = Field(default_factory=dict)
    type: str = Field(default="movie")
    num_mflix_comments: int = Field(default=0)
    lastupdated: Optional[str] = None
    plot_embedding: List[float] = Field(default_factory=list, description="Vector embedding of the plot")

    class Config(MongoBaseModel):
        pass
