# FastAPI Architecture

## Overview

This document explains the architecture of the FastAPI Starter project, demonstrating modern Python API development patterns.

---

## Architecture Pattern

```
Routes → Controllers → Services → Helpers
```

### Request Flow

```
Client Request
    ↓
Middleware (CORS, Error Handler)
    ↓
Route (validates input)
    ↓
Controller (handles request)
    ↓
Service (business logic)
    ↓
Helper (utilities, HTTP client)
    ↓
External API / Database
```

---

## Project Structure

This project is divided into two main parts: a **FastAPI Backend** and a **React Frontend**.

### 1. Backend (`backend/`)

```
backend/
├── app/              # FastAPI application logic
│   ├── main.py       # Initialization
│   ├── routes/       # API endpoints
│   ├── controllers/  # Request handlers
│   ├── services/     # Business logic
│   └── helpers/      # Utilities
└── tests/            # Pytest suite
```

### 2. Frontend (`frontend/`)

```
frontend/
├── src/
│   ├── components/   # UI components
│   ├── pages/        # Views
│   ├── services/     # RTK Query API slices
│   └── App.tsx       # Routing
└── tailwind.config.ts # Styling
```

---

## Layer Responsibilities

### 1. Routes (`backend/app/routes/`)

**Purpose**: Define API endpoints and validate requests

```python
# app/routes/health.py
from fastapi import APIRouter
from app.controllers import health_controller

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("")
async def health_check():
    return await health_controller.get_health()
```

**Responsibilities**:

- Define endpoints (`@router.get`, `@router.post`)
- Validate input with Pydantic models
- Call controllers
- Return responses

---

### 2. Controllers (`backend/app/controllers/`)

**Purpose**: Handle HTTP requests and responses

```python
# app/controllers/health_controller.py
async def get_health():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }
```

**Responsibilities**:

- Handle request logic
- Call services
- Format responses
- Handle errors

---

### 3. Services (`backend/app/services/`)

**Purpose**: Business logic and external integrations

```python
# app/services/external_api_service.py
class ExternalAPIService:
    async def get_posts(self, limit: int):
        url = f"{settings.JSONPLACEHOLDER_URL}/posts"
        data = await http_client.get(url)
        return data[:limit]
```

**Responsibilities**:

- Business logic
- External API calls
- Data transformation

---

### 4. Helpers (`backend/app/helpers/`)

**Purpose**: Reusable utility functions

```python
# app/helpers/http_client.py
async def get(url: str):
    response = await client.get(url)
    return response.json()
```

**Responsibilities**:

- HTTP client wrapper
- Logging configuration
- Common utilities

---

### 5. Middleware (`backend/app/middleware/`)

**Purpose**: Request/response processing

```python
# app/middleware/error_handler.py
async def error_handler_middleware(request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        logger.error(f"Error: {e}")
        return JSONResponse(status_code=500, content={"error": "Internal Server Error"})
```

**Responsibilities**:

- Global error handling
- CORS
- Authentication (if needed)
- Logging

---

## Key Design Patterns

### 1. Layered Architecture

Separates concerns into distinct layers for maintainability.

### 2. Dependency Injection

FastAPI's built-in DI system for managing dependencies.

### 3. Singleton Pattern

Services and helpers use singleton pattern for resource efficiency.

### 4. Repository Pattern

Services abstract data access and external API calls.

---

## Configuration Management

```python
# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Starter"
    DEBUG: bool = True
    PORT: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()
```

**Features**:

- Environment variables
- Type validation
- Default values
- `.env` file support

---

## Error Handling Strategy

### 1. Global Middleware

Catches all unhandled exceptions

### 2. HTTP Exceptions

FastAPI's `HTTPException` for API errors

### 3. Pydantic Validation

Automatic request validation

```python
from fastapi import HTTPException

async def get_post(post_id: int):
    if post_id < 1:
        raise HTTPException(status_code=400, detail="Invalid post ID")
```

---

## Async/Await Pattern

All I/O operations use async/await for non-blocking execution:

```python
async def fetch_data():
    # Non-blocking HTTP request
    response = await http_client.get(url)
    return response
```

**Benefits**:

- Better performance
- Handle multiple requests concurrently
- Efficient resource usage

---

## Testing Strategy

```python
# tests/test_api.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == 200
```

**Approach**:

- Integration tests for API endpoints
- Async test support with pytest-asyncio
- Mock external API calls

---

## Comparison with Node.js/Express

| Aspect          | Express.js                  | FastAPI                |
| --------------- | --------------------------- | ---------------------- |
| **Routing**     | `app.get('/path', handler)` | `@router.get("/path")` |
| **Validation**  | Manual or libraries         | Built-in (Pydantic)    |
| **Async**       | Promises/async-await        | async/await            |
| **Docs**        | Manual or Swagger           | Auto-generated         |
| **Type Safety** | TypeScript (optional)       | Type hints (built-in)  |

---
