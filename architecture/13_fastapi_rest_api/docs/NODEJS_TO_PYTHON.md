# 🔄 Node.js to Python FastAPI - Quick Reference Guide

## 📦 Package Management: package.json → pyproject.toml

### Node.js (package.json)

```json
{
  "name": "my-api",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.18.0",
    "axios": "^1.0.0"
  },
  "devDependencies": {
    "nodemon": "^2.0.0",
    "jest": "^29.0.0"
  }
}
```

### Python (pyproject.toml)

```toml
[project]
name = "fastapi-starter"
version = "1.0.0"
dependencies = ["fastapi>=0.109.0", "uvicorn>=0.27.0"]

# Like "devDependencies" in package.json
[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "ruff>=0.1.0",
]
```

**Key Differences:**

| Node.js               | Python (UV)                            | Purpose                  |
| --------------------- | -------------------------------------- | ------------------------ |
| `npm install`         | `uv sync`                              | Install all dependencies |
| `npm install express` | `uv add fastapi`                       | Add a dependency         |
| `npm install -D jest` | `uv add --dev pytest`                  | Add dev dependency       |
| `npm run dev`         | `uv run uvicorn app.main:app --reload` | Run dev server           |
| `npm test`            | `uv run pytest`                        | Run tests                |
| `package-lock.json`   | `uv.lock`                              | Lock file                |

---

## 🚀 Application Entry Point

### Node.js (index.js or server.js)

```javascript
// index.js - Entry point
const express = require("express");
const app = express();

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
```

### Python (app/main.py)

```python
# app/main.py - Entry point
from fastapi import FastAPI

app = FastAPI()

# Run with: uv run uvicorn app.main:app --reload
# Or in code:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
```

**Where to find it:**

- 📍 **Entry point**: `app/main.py` (like `index.js` in Node.js)
- 📍 **Dependencies**: `pyproject.toml` (like `package.json`)
- 📍 **Lock file**: `uv.lock` (like `package-lock.json`)

---

## 📁 Project Structure Comparison

### Node.js/Express Structure

```
my-api/
├── package.json          # Dependencies
├── index.js              # Entry point
├── routes/               # Route definitions
│   └── users.js
├── controllers/          # Request handlers
│   └── userController.js
├── services/             # Business logic
│   └── userService.js
├── utils/                # Helper functions
│   └── logger.js
└── middleware/           # Middleware
    └── errorHandler.js
```

### Python/FastAPI Structure (Simplified)

```
fastapi-starter/
├── pyproject.toml        # Dependencies (like package.json)
├── app/
│   ├── main.py           # Entry point (like index.js)
│   ├── config.py         # Configuration
│   ├── routes/           # Route definitions (like Express routes)
│   │   ├── health.py
│   │   └── external_api.py
│   ├── controllers/      # Request handlers (like Express controllers)
│   │   ├── health_controller.py
│   │   └── external_controller.py
│   ├── services/         # Business logic (same as Node.js)
│   │   └── external_api_service.py
│   ├── helpers/          # Helper functions (like utils in Node.js)
│   │   ├── http_client.py
│   │   └── logger.py
│   └── middleware/       # Middleware (same as Node.js)
│       └── error_handler.py
└── tests/                # Tests
    └── test_api.py
```

---

## 🛣️ Routes → Controllers → Services Pattern

### Node.js/Express

```javascript
// routes/users.js
const express = require("express");
const router = express.Router();
const userController = require("../controllers/userController");

router.get("/users", userController.getUsers);

module.exports = router;

// controllers/userController.js
const userService = require("../services/userService");

exports.getUsers = async (req, res) => {
  try {
    const users = await userService.fetchUsers();
    res.json(users);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// services/userService.js
const axios = require("axios");

exports.fetchUsers = async () => {
  const response = await axios.get("https://api.example.com/users");
  return response.data;
};
```

### Python/FastAPI (New Structure)

```python
# routes/users.py
from fastapi import APIRouter
from app.controllers import user_controller

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("")
async def get_users():
    return await user_controller.get_users()

# controllers/user_controller.py
from app.services import user_service

async def get_users():
    """Handle GET /users request"""
    try:
        users = await user_service.fetch_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# services/user_service.py
from app.helpers.http_client import http_client

async def fetch_users():
    """Business logic for fetching users"""
    response = await http_client.get('https://api.example.com/users')
    return response
```

---

## 🔑 Key Concepts Mapping

### 1. Importing Modules

**Node.js:**

```javascript
const express = require("express"); // CommonJS
import express from "express"; // ES6
```

**Python:**

```python
from fastapi import FastAPI                # Import specific item
import fastapi                             # Import module
from app.services import user_service      # Import from local module
```

### 2. Async/Await (Same!)

**Node.js:**

```javascript
async function fetchData() {
  const response = await axios.get(url);
  return response.data;
}
```

**Python:**

```python
async def fetch_data():
    response = await http_client.get(url)
    return response
```

### 3. Environment Variables

**Node.js:**

```javascript
require("dotenv").config();
const PORT = process.env.PORT || 3000;
```

**Python:**

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PORT: int = 8000

    class Config:
        env_file = ".env"
```

### 4. Middleware

**Node.js:**

```javascript
app.use((req, res, next) => {
  console.log("Request received");
  next();
});
```

**Python:**

```python
@app.middleware("http")
async def log_requests(request, call_next):
    print('Request received')
    response = await call_next(request)
    return response
```

---

## 📖 Where to Read What

### Dependencies & Scripts

- 📍 **File**: `pyproject.toml`
- 📍 **Section**: `[project.dependencies]` (like `dependencies` in package.json)
- 📍 **Dev Dependencies**: `[project.optional-dependencies.dev]` (like `devDependencies`)

### Entry Point & App Initialization

- 📍 **File**: `app/main.py`
- 📍 **Look for**: `app = FastAPI()` (like `const app = express()`)
- 📍 **Run command**: `uv run uvicorn app.main:app --reload`

### Routes/Endpoints

- 📍 **Folder**: `app/routes/`
- 📍 **Look for**: `@router.get()`, `@router.post()` decorators
- 📍 **Registered in**: `app/main.py` with `app.include_router()`

### Controllers (Request Handlers)

- 📍 **Folder**: `app/controllers/`
- 📍 **Purpose**: Handle HTTP requests, call services
- 📍 **Like**: Express controllers

### Services (Business Logic)

- 📍 **Folder**: `app/services/`
- 📍 **Purpose**: Business logic, external API calls
- 📍 **Like**: Node.js services

### Helpers/Utils

- 📍 **Folder**: `app/helpers/`
- 📍 **Purpose**: Reusable utility functions
- 📍 **Like**: `utils/` in Node.js

### Configuration

- 📍 **File**: `app/config.py`
- 📍 **Purpose**: Environment variables, settings
- 📍 **Like**: `config.js` in Node.js

---

## 🎯 Quick Command Reference

| Task                     | Node.js               | Python (UV)                            |
| ------------------------ | --------------------- | -------------------------------------- |
| **Install dependencies** | `npm install`         | `uv sync`                              |
| **Add dependency**       | `npm install express` | `uv add fastapi`                       |
| **Add dev dependency**   | `npm install -D jest` | `uv add --dev pytest`                  |
| **Run dev server**       | `npm run dev`         | `uv run uvicorn app.main:app --reload` |
| **Run tests**            | `npm test`            | `uv run pytest`                        |
| **Run script**           | `npm run script-name` | `uv run python script.py`              |

---

## 📚 File Reading Order (For Learning)

1. **`pyproject.toml`** - Understand dependencies (like package.json)
2. **`app/main.py`** - See how the app starts (like index.js)
3. **`app/config.py`** - Configuration setup
4. **`app/routes/health.py`** - Simple route example
5. **`app/controllers/health_controller.py`** - Request handler
6. **`app/services/external_api_service.py`** - Business logic
7. **`app/helpers/http_client.py`** - Utility functions

---

## 🔍 Key Differences to Remember

| Aspect              | Node.js                      | Python                         |
| ------------------- | ---------------------------- | ------------------------------ |
| **Package file**    | `package.json`               | `pyproject.toml`               |
| **Entry point**     | `index.js` or `server.js`    | `app/main.py`                  |
| **Import**          | `require()` or `import`      | `import` or `from ... import`  |
| **Export**          | `module.exports` or `export` | No export needed (just import) |
| **Async**           | `async/await`                | `async/await` (same!)          |
| **Run server**      | `node index.js`              | `uvicorn app.main:app`         |
| **Package manager** | `npm` or `yarn`              | `uv` or `pip`                  |

---

## 💡 Pro Tips

1. **No `models/` folder needed** if you're not using a database
   - Use Pydantic models inline in routes/controllers for validation

2. **Folder naming**:
   - Use `helpers/` or `utils/` (both are fine)
   - Use `routes/` or `routers/` (both are fine)

3. **Import paths**:
   - `from app.services import user_service` (absolute import)
   - Better than relative imports like `from ..services import user_service`

4. **Running the app**:
   - Development: `uv run uvicorn app.main:app --reload`
   - Production: `uv run uvicorn app.main:app --host 0.0.0.0 --port 8000`

---

This guide should help you navigate the Python/FastAPI project with your Node.js knowledge! 🚀
