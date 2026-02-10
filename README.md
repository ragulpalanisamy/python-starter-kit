# 🐍 Python Starter Kit

> **Learn Python with a clean, simple project structure**

A beginner-friendly Python starter kit for learning and practicing Python programming.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📁 Project Structure

```
python-starter-kit/
├── starter_kit/           # Basic Python learning
│   ├── tests/             # Tests for operations
│   ├── examples/          # Example scripts
│   ├── operations.py
│   └── __init__.py
├── fastapi-starter/       # Full-stack FastAPI + React project
│   ├── backend/           # FastAPI REST API
│   ├── frontend/          # React + Tailwind Frontend
│   └── architecture/      # Specific architecture docs
├── architecture/         # General learning resources
│   ├── python-basics/    # Python fundamentals
│   └── fastapi-rest-api/ # FastAPI architecture
└── README.md            # This file
```

---

## 🚀 Quick Start

### 1. Install UV Package Manager

```bash
# macOS/Linux
brew install uv

# Windows
powershell -c "irmo https://astral.sh/uv/install.ps1 | iex"
```

### 2. Setup & Run

```bash
# Navigate to starter kit
cd starter_kit

# Sync dependencies (uses UV)
uv sync

# Run an example
uv run examples/basic_operations.py
```

### 4. Try It Yourself

```python
# Import the functions
from starter_kit.operations import add, subtract, multiply, divide

# Use them
print(add(5, 3))        # Output: 8
print(multiply(4, 7))   # Output: 28
```

---

## 📚 What's Inside

### `starter_kit/` - Your Code

- **`operations.py`** - Basic math functions (add, subtract, multiply, divide)
- **`__init__.py`** - Makes it importable as a package

### `starter_kit/tests/` - Test Your Code

- **`test_operations.py`** - Tests to make sure code works correctly
- Run with: `uv run pytest`

### `starter_kit/examples/` - Learn by Example

- **`basic_operations.py`** - Shows how to use the functions

### `architecture/` - Learn Python Internals

- **`python-basics/`** - Visual guides explaining how Python executes code
- **`fastapi-rest-api/`** - FastAPI architecture and REST API concepts
- Great for understanding what happens behind the scenes!

### `fastapi-starter/` - Production-Ready API

- **Modern FastAPI REST API** with clean architecture
- Routes → Controllers → Services → Helpers pattern
- External API integration examples
- Auto-generated API documentation
- See `fastapi-starter/README.md` for details

---

## 🎓 Learning Path

### Beginner: Python Basics

1. **Read the architecture docs** → `architecture/python-basics/index.md`
2. **Study the code** → `starter_kit/operations.py`
3. **Run the example** → `cd starter_kit && uv run examples/basic_operations.py`
4. **Try writing your own function** → Add to `starter_kit/operations.py`
5. **Write tests** → Add to `starter_kit/tests/test_operations.py`

### Intermediate: FastAPI + React Full-stack

1. **Read FastAPI architecture** → `architecture/fastapi-rest-api/index.md`
2. **Explore the project** → `cd fastapi-starter`
3. **Run the Backend** → `cd backend && uv run uvicorn app.main:app --reload`
4. **Run the Frontend** → `cd frontend && npm run dev`
5. **Try the API docs** → http://localhost:8000/docs
6. **Build your own features** → Follow the patterns in `backend/app/routes/` and `frontend/src/`

---

## 💡 Key Concepts Demonstrated

### Python Basics (`starter_kit/`)

✅ **Project Organization** - Clean folder structure  
✅ **Functions** - Reusable code blocks  
✅ **Type Hints** - `def add(a: float, b: float) -> float:`  
✅ **Docstrings** - Document your code  
✅ **Testing** - Make sure code works  
✅ **Imports** - Use code from other files  
✅ **Virtual Environments** - Isolated dependencies

### FastAPI REST API (`fastapi-starter/`)

✅ **REST API** - Modern web service architecture  
✅ **Async/Await** - Non-blocking I/O operations  
✅ **Clean Architecture** - Separation of concerns  
✅ **Auto Documentation** - Swagger UI at `/docs`  
✅ **Type Safety** - Pydantic validation  
✅ **External APIs** - Integration examples  
✅ **UV Package Manager** - Modern Python tooling

---

## 📦 Projects Included

### 1. **starter_kit/** - Python Basics

Simple Python package for learning fundamentals

### 2. **fastapi-starter/** - Full-stack App

Production-ready FastAPI application with React frontend:

- **Backend**: Health check, External API integration, Clean architecture
- **Frontend**: Modern React, Tailwind CSS, Redux/API integration
- **Deployment**: Ready for Render (see `backend/render.yaml`)
- **Documentation**: Auto-generated Swagger docs

---

## 🔧 Common Commands

### Python Basics (`starter_kit/`)

```bash
# Navigate to starter kit
cd starter_kit

# Sync dependencies
uv sync

# Run example
uv run examples/basic_operations.py

# Run tests
uv run pytest

# Use Python interactive shell
uv run python
>>> from operations import add
>>> add(5, 3)
8
```

### FastAPI Project (`fastapi-starter/`)

```bash
# Navigate to backend
cd fastapi-starter/backend

# Install dependencies
uv sync

# Run development server
uv run uvicorn app.main:app --reload

# Navigate to frontend
cd ../frontend

# Install dependencies
npm install

# Run frontend
npm run dev
```

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 👤 Author

**Ragul P** - [@ragulpalanisamy](https://github.com/ragulpalanisamy)

---

_Happy Learning! 🚀_
