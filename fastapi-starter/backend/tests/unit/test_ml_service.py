import pytest
from app.modules.api.v1.ml.service import MLService

@pytest.fixture
def ml_service():
    # Use the default model for testing
    return MLService()

def test_ml_service_initialization(ml_service):
    assert ml_service.model_name == "distilbert-base-uncased-finetuned-sst-2-english"
    assert ml_service.classifier is None

def test_ml_service_load_model(ml_service):
    ml_service.load_model()
    assert ml_service.classifier is not None

def test_ml_service_predict_single(ml_service):
    text = "I love this project!"
    result = ml_service.predict_single(text)
    
    assert result["text"] == text
    assert "sentiment" in result
    assert "confidence" in result
    assert result["model_version"] == ml_service.model_name
    assert "processing_time_ms" in result

def test_ml_service_predict_batch(ml_service):
    texts = ["This is great!", "I don't like this."]
    results = ml_service.predict_batch(texts)
    
    assert len(results) == 2
    for i, text in enumerate(texts):
        assert results[i]["text"] == text
        assert "sentiment" in results[i]
        assert "confidence" in results[i]

def test_ml_service_get_model_info(ml_service):
    info = ml_service.get_model_info()
    assert info["model_name"] == ml_service.model_name
    assert "device" in info
    assert info["framework"] == "PyTorch"
