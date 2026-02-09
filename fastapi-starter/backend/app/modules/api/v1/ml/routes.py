"""ML prediction API endpoints using PyTorch."""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
from datetime import datetime
import os
import sys

from .service import ml_service
from .controller import MLController
from app.db.mongodb import get_mongodb
from app.utils.prediction_repository import PredictionRepository
from app.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

# Dependency to get ML controller
async def get_ml_controller(mongodb = Depends(get_mongodb)):
    repo = PredictionRepository(mongodb)
    return MLController(ml_service, repo)

from app.validations.ml_schema import PredictRequest, BatchPredictRequest, PredictionResponse

@router.post("/predict", response_model=PredictionResponse)
async def predict_sentiment(
    request: PredictRequest,
    controller: MLController = Depends(get_ml_controller)
):
    """Predict sentiment for a single text."""
    return await controller.predict_sentiment(request.text)


@router.post("/batch-predict")
async def batch_predict_sentiment(
    request: BatchPredictRequest,
    controller: MLController = Depends(get_ml_controller)
):
    """Predict sentiment for multiple texts."""
    return await controller.batch_predict_sentiment(request.texts)


@router.get("/model-info")
async def get_model_info(controller: MLController = Depends(get_ml_controller)):
    """Get ML model information."""
    return await controller.get_model_info()


@router.get("/health")
async def ml_health_check(controller: MLController = Depends(get_ml_controller)):
    """Check ML service health."""
    return await controller.ml_health_check()


@router.get("/history")
async def get_prediction_history(
    skip: int = 0,
    limit: int = 10,
    sentiment: Optional[str] = None,
    controller: MLController = Depends(get_ml_controller)
):
    """Get prediction history with pagination."""
    return await controller.get_prediction_history(skip, limit, sentiment)


@router.get("/stats")
async def get_prediction_stats(controller: MLController = Depends(get_ml_controller)):
    """Get prediction statistics."""
    return await controller.get_prediction_stats()


@router.delete("/{prediction_id}")
async def delete_prediction(
    prediction_id: str,
    controller: MLController = Depends(get_ml_controller)
):
    """Delete a prediction."""
    return await controller.delete_prediction(prediction_id)
