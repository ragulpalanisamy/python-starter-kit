import uuid
from datetime import datetime
from typing import List, Optional, Dict, Any
from fastapi import HTTPException
from .service import MLService
from app.utils.prediction_repository import PredictionRepository
from app.Models.domain_models import PredictionModel
from app.utils.logger import get_logger

logger = get_logger(__name__)

from app.config.settings import settings

class MLController:
    """Controller for ML prediction endpoints."""
    
    def __init__(self, ml_service: MLService, prediction_repository: PredictionRepository):
        self.ml_service = ml_service
        self.repo = prediction_repository

    async def predict_sentiment(self, text: str) -> Dict[str, Any]:
        """Predict sentiment for a single text."""
        if not settings.ENABLE_ML:
            raise HTTPException(status_code=503, detail="ML service is disabled (ENABLE_ML=False)")
            
        if self.ml_service is None:
            raise HTTPException(status_code=503, detail="ML service not available")
        
        try:
            # Make prediction
            result = self.ml_service.predict_single(text)
            
            # Generate prediction ID
            prediction_id = str(uuid.uuid4())
            
            # Create PredictionModel instance
            prediction = PredictionModel(
                prediction_id=prediction_id,
                text=result["text"],
                sentiment=result["sentiment"],
                confidence=result["confidence"],
                model_version=result["model_version"],
                processing_time_ms=result["processing_time_ms"],
                created_at=datetime.utcnow()
            )
            
            # Save to MongoDB
            await self.repo.create_prediction(prediction)
            
            logger.info(f"Prediction created: {prediction_id}")
            
            return {
                "prediction_id": prediction_id,
                **result,
                "created_at": prediction.created_at
            }
        except Exception as e:
            logger.error(f"Prediction failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def batch_predict_sentiment(self, texts: List[str]) -> Dict[str, Any]:
        """Predict sentiment for multiple texts."""
        if not settings.ENABLE_ML:
            raise HTTPException(status_code=503, detail="ML service is disabled (ENABLE_ML=False)")

        if self.ml_service is None:
            raise HTTPException(status_code=503, detail="ML service not available")
        
        try:
            # Generate batch ID
            batch_id = str(uuid.uuid4())
            
            # Make batch prediction
            results = self.ml_service.predict_batch(texts)
            
            # Save all predictions to MongoDB
            predictions = []
            
            for result in results:
                prediction_id = str(uuid.uuid4())
                prediction = PredictionModel(
                    prediction_id=prediction_id,
                    text=result["text"],
                    sentiment=result["sentiment"],
                    confidence=result["confidence"],
                    model_version=result["model_version"],
                    batch_id=batch_id,
                    processing_time_ms=result["processing_time_ms"],
                    created_at=datetime.utcnow()
                )
                
                await self.repo.create_prediction(prediction)
                predictions.append({
                    "prediction_id": prediction_id,
                    **result,
                    "created_at": prediction.created_at
                })
            
            logger.info(f"Batch prediction created: {batch_id} ({len(predictions)} texts)")
            
            return {
                "batch_id": batch_id,
                "predictions": predictions,
                "total": len(predictions)
            }
        except Exception as e:
            logger.error(f"Batch prediction failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def get_model_info(self) -> Dict[str, Any]:
        """Get ML model information."""
        if not settings.ENABLE_ML:
             return {
                "model_name": "disabled",
                "enabled": False,
                "message": "ML features are currently disabled"
            }

        if self.ml_service is None:
            raise HTTPException(status_code=503, detail="ML service not available")
        
        try:
            return self.ml_service.get_model_info()
        except Exception as e:
            logger.error(f"Failed to get model info: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def ml_health_check(self) -> Dict[str, Any]:
        """Check ML service health."""
        if not settings.ENABLE_ML:
            return {
                "status": "disabled",
                "model_loaded": False,
                "message": "ML features are disabled via configuration"
            }

        if self.ml_service is None:
            return {
                "status": "unhealthy",
                "model_loaded": False,
                "error": "Predictor not initialized"
            }
        
        try:
            info = self.ml_service.get_model_info()
            return {
                "status": "healthy",
                "model_loaded": True,
                **info
            }
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return {
                "status": "unhealthy",
                "model_loaded": False,
                "error": str(e)
            }

    async def get_prediction_history(self, skip: int, limit: int, sentiment: Optional[str] = None) -> Dict[str, Any]:
        """Get prediction history with pagination."""
        try:
            predictions = await self.repo.list_predictions(
                skip=skip,
                limit=limit,
                sentiment=sentiment
            )
            
            return {
                "predictions": [p.dict() for p in predictions],
                "skip": skip,
                "limit": limit
            }
        except Exception as e:
            logger.error(f"Failed to get history: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def get_prediction_stats(self) -> Dict[str, Any]:
        """Get prediction statistics."""
        try:
            return await self.repo.get_prediction_stats()
        except Exception as e:
            logger.error(f"Failed to get stats: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    async def delete_prediction(self, prediction_id: str) -> Dict[str, Any]:
        """Delete a prediction."""
        try:
            deleted = await self.repo.delete_prediction(prediction_id)
            if not deleted:
                raise HTTPException(status_code=404, detail="Prediction not found")
            
            logger.info(f"Prediction deleted: {prediction_id}")
            
            return {
                "prediction_id": prediction_id,
                "message": "Prediction deleted successfully"
            }
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Failed to delete prediction: {e}")
            raise HTTPException(status_code=500, detail=str(e))
