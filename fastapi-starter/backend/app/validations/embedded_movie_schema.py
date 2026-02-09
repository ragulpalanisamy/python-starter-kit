from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field

class EmbeddedMovieCreate(BaseModel):
    """Schema for creating an embedded movie."""
    title: str = Field(..., description="The title of the movie")
    year: int = Field(..., description="Release year")
    plot: Optional[str] = None
    fullplot: Optional[str] = None
    genres: List[str] = Field(default_factory=list)
    runtime: Optional[int] = None
    cast: List[str] = Field(default_factory=list)
    languages: List[str] = Field(default_factory=list)
    released: Optional[datetime] = None
    directors: List[str] = Field(default_factory=list)
    writers: List[str] = Field(default_factory=list)
    countries: List[str] = Field(default_factory=list)
    awards: Dict[str, Any] = Field(default_factory=dict)
    imdb: Dict[str, Any] = Field(default_factory=dict)
    type: str = "movie"
    plot_embedding: List[float] = Field(default_factory=list)

class EmbeddedMovieUpdate(BaseModel):
    """Schema for updating an embedded movie."""
    title: Optional[str] = None
    year: Optional[int] = None
    plot: Optional[str] = None
    fullplot: Optional[str] = None
    genres: Optional[List[str]] = None
    runtime: Optional[int] = None
    cast: Optional[List[str]] = None
    languages: Optional[List[str]] = None
    released: Optional[datetime] = None
    directors: Optional[List[str]] = None
    writers: Optional[List[str]] = None
    countries: Optional[List[str]] = None
    awards: Optional[Dict[str, Any]] = None
    imdb: Optional[Dict[str, Any]] = None
    plot_embedding: Optional[List[float]] = None
