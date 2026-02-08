"""
API Tests

This module contains tests for the FastAPI endpoints.
It uses pytest and httpx for async testing.

To run these tests:
    uv run pytest tests/test_api.py -v
"""

import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_root_endpoint():
    """
    Test the root endpoint returns welcome message.
    
    This test verifies that:
    - The root endpoint is accessible
    - It returns a 200 OK status
    - The response contains expected fields
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert "docs" in data


@pytest.mark.asyncio
async def test_health_check():
    """
    Test the basic health check endpoint.
    
    This verifies that:
    - The health endpoint is accessible
    - It returns a healthy status
    - The response includes a timestamp
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


@pytest.mark.asyncio
async def test_detailed_health_check():
    """
    Test the detailed health check endpoint.
    
    This verifies that:
    - The detailed health endpoint is accessible
    - It returns system information
    - Dependencies are reported
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health/detailed")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data
    assert "python_version" in data
    assert "dependencies" in data


@pytest.mark.asyncio
async def test_external_api():
    """
    Test the external API endpoints.
    
    Tests that:
    - The external API endpoints return valid responses
    - The data structure matches expectations
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Test posts endpoint
        response = await client.get("/api/v1/external/posts?limit=5")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) <= 5


# Note: External API tests are commented out to avoid making real API calls during testing
# In a production environment, you would mock these external API calls

# @pytest.mark.asyncio
# async def test_get_posts():
#     """Test fetching posts from JSONPlaceholder."""
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         response = await client.get("/api/v1/external/posts?limit=5")
#     
#     assert response.status_code == 200
#     data = response.json()
#     assert isinstance(data, list)
#     assert len(data) <= 5
