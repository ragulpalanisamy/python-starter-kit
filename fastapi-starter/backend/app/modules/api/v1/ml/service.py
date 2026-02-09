from typing import List, Dict, Any
import time

from app.utils.logger import get_logger

logger = get_logger(__name__)

class MLService:
    """Service for running ML predictions."""
    
    def __init__(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english"): 
        """
        Initialize the ML service.
        """ 
        self.model_name = model_name
        self.classifier = None
        self._device_cache = None
        logger.info(f"MLService initialized (lazy-loading enabled for {model_name})")

    @property
    def device(self):
        """Lazy-loaded device info."""
        if self._device_cache is None:
            try:
                import torch
                self._device_cache = "cuda" if torch.cuda.is_available() else "cpu"
            except ImportError:
                self._device_cache = "cpu"
        return self._device_cache
            
    def load_model(self):
        """Load the model if not already loaded."""
        if self.classifier is None:
            try:
                from transformers import pipeline
                logger.info(f"Loading ML model: {self.model_name} on {self.device}")
                self.classifier = pipeline(
                    "sentiment-analysis",
                    model=self.model_name,
                    device=-1 if self.device == "cpu" else 0
                )
                logger.info("Model loaded successfully")
            except Exception as e:
                logger.error(f"Failed to load model: {e}")
                raise

    def predict_single(self, text: str) -> Dict[str, Any]:
        """
        Predict sentiment for a single text.
        
        Args:
            text: Input text
            
        Returns:
            Prediction result
        """
        if self.classifier is None:
            self.load_model()
            
        start_time = time.time()
        result = self.classifier(text)[0]
        processing_time = (time.time() - start_time) * 1000
        
        return {
            "text": text,
            "sentiment": result["label"],
            "confidence": round(result["score"], 4),
            "model_version": self.model_name,
            "processing_time_ms": round(processing_time, 2)
        }

    def predict_batch(self, texts: List[str]) -> List[Dict[str, Any]]:
        """
        Predict sentiment for a batch of texts.
        
        Args:
            texts: List of input texts
            
        Returns:
            List of prediction results
        """
        if self.classifier is None:
            self.load_model()
            
        start_time = time.time()
        results = self.classifier(texts)
        processing_time_total = (time.time() - start_time) * 1000
        processing_time_per_item = processing_time_total / len(texts)
        
        formatted_results = []
        for text, result in zip(texts, results):
            formatted_results.append({
                "text": text,
                "sentiment": result["label"],
                "confidence": round(result["score"], 4),
                "model_version": self.model_name,
                "processing_time_ms": round(processing_time_per_item, 2)
            })
            
        return formatted_results

    def get_model_info(self) -> Dict[str, Any]:
        """Get model information."""
        return {
            "model_name": self.model_name,
            "device": self.device,
            "framework": "PyTorch",
            "task": "sentiment-analysis"
        }

# Singleton instance
ml_service = MLService()
