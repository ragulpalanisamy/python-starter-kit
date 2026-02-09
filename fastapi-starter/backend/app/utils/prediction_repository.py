"""Repository for ML prediction operations."""

from typing import List, Optional
from datetime import datetime
from app.db.mongodb import MongoDB
from app.Models.domain_models import PredictionModel
from app.utils.logger import get_logger

logger = get_logger(__name__)


class PredictionRepository:
    """Repository for managing ML predictions in MongoDB."""
    
    def __init__(self, mongodb: MongoDB):
        """
        Initialize repository.
        
        Args:
            mongodb: MongoDB instance
        """
        self.mongodb = mongodb
        self.collection = mongodb.get_collection("predictions")
    
    async def create_prediction(self, prediction: PredictionModel) -> str:
        """
        Create a new prediction record.
        
        Args:
            prediction: Prediction model instance
            
        Returns:
            prediction_id of the created record
        """
        try:
            result = await self.collection.insert_one(
                prediction.dict(by_alias=True, exclude={"id"})
            )
            logger.info(f"Created prediction record: {prediction.prediction_id}")
            return prediction.prediction_id
        except Exception as e:
            logger.error(f"Error creating prediction: {e}")
            raise
    
    async def get_prediction(self, prediction_id: str) -> Optional[PredictionModel]:
        """
        Get prediction by ID.
        
        Args:
            prediction_id: Prediction identifier
            
        Returns:
            Prediction model or None
        """
        try:
            prediction_data = await self.collection.find_one({"prediction_id": prediction_id})
            if prediction_data:
                return PredictionModel(**prediction_data)
            return None
        except Exception as e:
            logger.error(f"Error getting prediction {prediction_id}: {e}")
            raise
    
    async def list_predictions(
        self,
        skip: int = 0,
        limit: int = 10,
        sentiment: Optional[str] = None,
        batch_id: Optional[str] = None
    ) -> List[PredictionModel]:
        """
        List predictions with pagination.
        
        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            sentiment: Optional sentiment filter
            batch_id: Optional batch ID filter
            
        Returns:
            List of prediction models
        """
        try:
            query = {}
            if sentiment:
                query["sentiment"] = sentiment
            if batch_id:
                query["batch_id"] = batch_id
            
            cursor = self.collection.find(query).sort("created_at", -1).skip(skip).limit(limit)
            prediction_dicts = await cursor.to_list(length=limit)
            
            return [PredictionModel(**p) for p in prediction_dicts]
        except Exception as e:
            logger.error(f"Error listing predictions: {e}")
            raise
    
    async def get_prediction_stats(self) -> dict:
        """
        Get comprehensive prediction statistics with multiple dimensions.
        
        Returns:
            Dictionary with prediction stats including:
            - total: Total number of predictions
            - by_sentiment: Count and avg confidence by sentiment
            - by_date: Daily prediction counts (last 30 days)
            - confidence_distribution: Distribution of confidence scores
            - avg_processing_time: Average processing time
            - recent_trends: Hourly trends for last 24 hours
        """
        try:
            from datetime import datetime, timedelta
            from collections import defaultdict
            
            # Basic sentiment stats
            sentiment_pipeline = [
                {
                    "$group": {
                        "_id": "$sentiment",
                        "count": {"$sum": 1},
                        "avg_confidence": {"$avg": "$confidence"},
                        "avg_processing_time": {"$avg": "$processing_time_ms"}
                    }
                }
            ]
            
            sentiment_results = await self.collection.aggregate(sentiment_pipeline).to_list(length=None)
            
            stats = {
                "total": await self.collection.count_documents({}),
                "by_sentiment": {},
                "by_date": [],
                "confidence_distribution": {
                    "high": 0,  # >= 0.8
                    "medium": 0,  # 0.5-0.8
                    "low": 0  # < 0.5
                },
                "avg_processing_time": 0,
                "recent_trends": []
            }
            
            # Process sentiment stats
            total_processing_time = 0
            total_count = 0
            for result in sentiment_results:
                sentiment = result["_id"]
                count = result["count"]
                stats["by_sentiment"][sentiment] = {
                    "count": count,
                    "avg_confidence": round(result["avg_confidence"], 3),
                    "avg_processing_time": round(result["avg_processing_time"], 2)
                }
                total_processing_time += result["avg_processing_time"] * count
                total_count += count
            
            if total_count > 0:
                stats["avg_processing_time"] = round(total_processing_time / total_count, 2)
            
            # Date-based stats (last 30 days)
            thirty_days_ago = datetime.utcnow() - timedelta(days=30)
            date_pipeline = [
                {
                    "$match": {
                        "created_at": {"$gte": thirty_days_ago}
                    }
                },
                {
                    "$group": {
                        "_id": {
                            "$dateToString": {
                                "format": "%Y-%m-%d",
                                "date": "$created_at"
                            }
                        },
                        "count": {"$sum": 1},
                        "positive": {
                            "$sum": {"$cond": [{"$eq": ["$sentiment", "POSITIVE"]}, 1, 0]}
                        },
                        "negative": {
                            "$sum": {"$cond": [{"$eq": ["$sentiment", "NEGATIVE"]}, 1, 0]}
                        }
                    }
                },
                {"$sort": {"_id": 1}}
            ]
            
            date_results = await self.collection.aggregate(date_pipeline).to_list(length=None)
            stats["by_date"] = [
                {
                    "date": result["_id"],
                    "total": result["count"],
                    "positive": result["positive"],
                    "negative": result["negative"]
                }
                for result in date_results
            ]
            
            # Confidence distribution
            confidence_pipeline = [
                {
                    "$project": {
                        "confidence_bucket": {
                            "$cond": [
                                {"$gte": ["$confidence", 0.8]}, "high",
                                {"$cond": [
                                    {"$gte": ["$confidence", 0.5]}, "medium", "low"
                                ]}
                            ]
                        }
                    }
                },
                {
                    "$group": {
                        "_id": "$confidence_bucket",
                        "count": {"$sum": 1}
                    }
                }
            ]
            
            confidence_results = await self.collection.aggregate(confidence_pipeline).to_list(length=None)
            for result in confidence_results:
                bucket = result["_id"]
                if bucket in stats["confidence_distribution"]:
                    stats["confidence_distribution"][bucket] = result["count"]
            
            # Recent trends (last 24 hours by hour)
            twenty_four_hours_ago = datetime.utcnow() - timedelta(hours=24)
            trend_pipeline = [
                {
                    "$match": {
                        "created_at": {"$gte": twenty_four_hours_ago}
                    }
                },
                {
                    "$group": {
                        "_id": {
                            "$dateToString": {
                                "format": "%Y-%m-%d %H:00",
                                "date": "$created_at"
                            }
                        },
                        "count": {"$sum": 1}
                    }
                },
                {"$sort": {"_id": 1}}
            ]
            
            trend_results = await self.collection.aggregate(trend_pipeline).to_list(length=None)
            stats["recent_trends"] = [
                {
                    "hour": result["_id"],
                    "count": result["count"]
                }
                for result in trend_results
            ]
            
            return stats
        except Exception as e:
            logger.error(f"Error getting prediction stats: {e}")
            raise
    
    async def delete_prediction(self, prediction_id: str) -> bool:
        """
        Delete a prediction record.
        
        Args:
            prediction_id: Prediction identifier
            
        Returns:
            True if deleted successfully
        """
        try:
            result = await self.collection.delete_one({"prediction_id": prediction_id})
            if result.deleted_count > 0:
                logger.info(f"Deleted prediction: {prediction_id}")
                return True
            return False
        except Exception as e:
            logger.error(f"Error deleting prediction: {e}")
            raise
    
    async def delete_batch_predictions(self, batch_id: str) -> int:
        """
        Delete all predictions in a batch.
        
        Args:
            batch_id: Batch identifier
            
        Returns:
            Number of predictions deleted
        """
        try:
            result = await self.collection.delete_many({"batch_id": batch_id})
            logger.info(f"Deleted {result.deleted_count} predictions from batch {batch_id}")
            return result.deleted_count
        except Exception as e:
            logger.error(f"Error deleting batch predictions: {e}")
            raise
