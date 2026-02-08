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
│   ├── __init__.py
│   └── operations.py
├── fastapi-starter/       # FastAPI REST API project
│   ├── app/              # Application code
│   ├── tests/            # API tests
│   └── pyproject.toml    # Dependencies
├── architecture/         # Learning resources
│   ├── python-basics/    # Python fundamentals
│   └── fastapi-rest-api/ # FastAPI architecture
├── tests/                # Tests for starter_kit
├── examples/             # Example scripts
└── README.md            # This file
```

---

## 🚀 Quick Start

### 1. Setup Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

### 2. Install Dependencies (Optional)

```bash
pip install -r requirements.txt
```

### 3. Run Examples

```bash
# Run the example
python examples/basic_operations.py
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

### `tests/` - Test Your Code

- **`test_operations.py`** - Tests to make sure code works correctly
- Run with: `pytest` (install with `pip install pytest`)

### `examples/` - Learn by Example

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
3. **Run the example** → `python examples/basic_operations.py`
4. **Try writing your own function** → Add to `starter_kit/operations.py`
5. **Write tests** → Add to `tests/test_operations.py`

### Intermediate: FastAPI REST API

1. **Read FastAPI architecture** → `architecture/fastapi-rest-api/index.md`
2. **Explore the project** → `cd fastapi-starter`
3. **Run the API** → `uv run uvicorn app.main:app --reload`
4. **Try the API docs** → http://localhost:8000/docs
5. **Build your own endpoints** → Follow the patterns in `app/routes/`

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

### 2. **fastapi-starter/** - REST API

Production-ready FastAPI application with:

- Health check endpoints
- External API integration (JSONPlaceholder, Open-Meteo)
- Clean architecture pattern
- Comprehensive tests
- Auto-generated documentation

---

## 🔧 Common Commands

### Python Basics

```bash
# Activate virtual environment
source venv/bin/activate

# Run example
python examples/basic_operations.py

# Run tests (install pytest first)
pip install pytest
pytest

# Use Python interactive shell
python
>>> from starter_kit.operations import add
>>> add(5, 3)
8
```

### FastAPI Project

```bash
# Navigate to project
cd fastapi-starter

# Install dependencies
uv sync

# Run development server
uv run uvicorn app.main:app --reload

# Access API documentation
# Open http://localhost:8000/docs in browser

# Run tests
uv run pytest
```

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 👤 Author

**Ragul P** - [@ragulpalanisamy](https://github.com/ragulpalanisamy)

---

_Happy Learning! 🚀_
