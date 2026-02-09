"""Central export point for domain models."""

from app.Models.base import PyObjectId, MongoBaseModel
from app.Models.movie import MovieModel
from app.Models.comment import CommentModel
from app.Models.theater import TheaterModel
from app.Models.embedded_movie import EmbeddedMovieModel
from app.Models.user import UserModel
from app.Models.board import BoardModel
from app.Models.prediction import PredictionModel
from app.Models.data_models import DataUploadModel, ProcessedDataModel

# All key models exported here to maintain compatibility
__all__ = [
    "PyObjectId",
    "MongoBaseModel",
    "MovieModel",
    "CommentModel",
    "TheaterModel",
    "EmbeddedMovieModel",
    "UserModel",
    "BoardModel",
    "PredictionModel",
    "DataUploadModel",
    "ProcessedDataModel"
]
