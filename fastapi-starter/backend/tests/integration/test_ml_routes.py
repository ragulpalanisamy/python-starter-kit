import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.config.settings import settings

from unittest.mock import patch, MagicMock, AsyncMock

@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_ml_health_check(client):
    response = await client.get(f"{settings.API_V1_PREFIX}/ml/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["model_loaded"] is True

@pytest.mark.asyncio
async def test_ml_model_info(client):
    response = await client.get(f"{settings.API_V1_PREFIX}/ml/model-info")
    assert response.status_code == 200
    data = response.json()
    assert "model_name" in data

@pytest.mark.asyncio
async def test_predict_sentiment(client):
    with patch("app.modules.api.v1.ml.routes.PredictionRepository") as MockRepo:
        mock_repo = MagicMock()
        mock_repo.create_prediction = AsyncMock(return_value="test-id")
        MockRepo.return_value = mock_repo
        
        response = await client.post(
            f"{settings.API_V1_PREFIX}/ml/predict",
            json={"text": "FastAPI is amazing!"}
        )
        
    assert response.status_code == 200
    data = response.json()
    assert "prediction_id" in data
    assert data["text"] == "FastAPI is amazing!"
    assert "sentiment" in data
    assert "confidence" in data

@pytest.mark.asyncio
async def test_batch_predict_sentiment(client):
    with patch("app.modules.api.v1.ml.routes.PredictionRepository") as MockRepo:
        mock_repo = MagicMock()
        mock_repo.create_prediction = AsyncMock(return_value="test-id")
        MockRepo.return_value = mock_repo
        
        response = await client.post(
            f"{settings.API_V1_PREFIX}/ml/batch-predict",
            json={"texts": ["Good", "Bad"]}
        )
        
    assert response.status_code == 200
    data = response.json()
    assert "batch_id" in data
    assert len(data["predictions"]) == 2
