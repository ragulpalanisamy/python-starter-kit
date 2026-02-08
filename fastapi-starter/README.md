# 🚀 FastAPI Starter

> **Modern Python REST API with FastAPI and UV Package Manager**

A production-ready Python API demonstrating best practices with FastAPI and external API integration.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-009688.svg)](https://fastapi.tiangolo.com/)

---

## ✨ Features

✅ **Modern Stack** - FastAPI + UV package manager  
✅ **Clean Architecture** - Routes → Controllers → Services → Helpers  
✅ **External APIs** - JSONPlaceholder, Open-Meteo (no API keys!)  
✅ **Type Safety** - Full type hints with Pydantic validation  
✅ **Async/Await** - Non-blocking I/O for better performance  
✅ **Auto Documentation** - Swagger UI at `/docs`  
✅ **Testing** - Pytest with async support

---

## 📁 Project Structure

```
fastapi-ml-starter/
├── pyproject.toml           # Dependencies (like package.json)
├── app/
│   ├── main.py              # ⭐ Entry point
│   ├── config.py            # Configuration
│   ├── routes/              # Route definitions
│   ├── controllers/         # Request handlers
│   ├── services/            # Business logic
│   ├── helpers/             # Utilities
│   └── middleware/          # Middleware
└── tests/                   # Tests
```

**Pattern**: `Route → Controller → Service → Helper`

---

## 🚀 Quick Start

### 1. Install UV Package Manager

```bash
# Install UV (macOS/Linux)
brew install uv

# Verify
uv --version
```

### 2. Install Dependencies

```bash
cd fastapi-ml-starter
uv sync
```

### 3. Run Server

```bash
uv run uvicorn app.main:app --reload
```

Server starts at: **http://localhost:8000**

## 📚 API Endpoints

### Health

- `GET /health` - Basic health check
- `GET /health/detailed` - Detailed system info

### External APIs

- `GET /api/v1/external/posts` - Blog posts (JSONPlaceholder)
- `GET /api/v1/external/users` - Users (JSONPlaceholder)
- `POST /api/v1/external/weather` - Weather data (Open-Meteo)

---

## 💡 Usage Examples

### Get Weather Data

```bash
curl -X POST http://localhost:8000/api/v1/external/weather \
  -H "Content-Type: application/json" \
  -d '{"latitude": 13.0827, "longitude": 80.2707}'
```

---

## 🧪 Testing

```bash
# Run all tests
uv run pytest

# With coverage
uv run pytest --cov=app
```

---

## 🛠️ Common Commands

```bash
uv sync                              # Install dependencies
uv run uvicorn app.main:app --reload # Run dev server
uv run pytest                        # Run tests
uv add package-name                  # Add dependency
```

---

## 🎓 For Node.js Developers

| Node.js        | Python/FastAPI                         |
| -------------- | -------------------------------------- |
| `package.json` | `pyproject.toml`                       |
| `npm install`  | `uv sync`                              |
| `npm run dev`  | `uv run uvicorn app.main:app --reload` |
| `routes/`      | `routes/` (same!)                      |
| `async/await`  | `async/await` (same!)                  |

See [Node.js to Python Guide](../architecture/fastapi-rest-api/docs/NODEJS_TO_PYTHON.md) for details.

---

## 📖 Resources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [Pydantic Docs](https://docs.pydantic.dev/)

---

## 👤 Author

**Ragul P** - [@ragulpalanisamy](https://github.com/ragulpalanisamy)

---

_Happy Coding! 🚀_
