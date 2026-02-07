# 🐍 Python Starter Kit

> **Learn Python with a clean, simple project structure**

A beginner-friendly Python starter kit for learning and practicing Python programming.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📁 Project Structure

```
python-starter-kit/
├── starter_kit/           # Your Python code
│   ├── __init__.py       # Makes it a package
│   └── operations.py     # Math operations
├── tests/                # Test your code
│   └── test_operations.py
├── examples/             # Example scripts
│   └── basic_operations.py
├── architecture/         # Learn how Python works
│   ├── index.md
│   ├── architecture.png
│   └── platform.png
├── .gitignore           # Git ignore rules
├── requirements.txt     # Dependencies
├── LICENSE             # MIT License
└── README.md          # This file
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

- Visual guides explaining how Python executes code
- Platform independence diagrams
- Great for understanding what happens behind the scenes!

---

## 🎓 Learning Path

1. **Read the architecture docs** → `architecture/index.md`
2. **Study the code** → `starter_kit/operations.py`
3. **Run the example** → `python examples/basic_operations.py`
4. **Try writing your own function** → Add to `starter_kit/operations.py`
5. **Write tests** → Add to `tests/test_operations.py`

---

## 💡 Key Concepts Demonstrated

✅ **Project Organization** - Clean folder structure  
✅ **Functions** - Reusable code blocks  
✅ **Type Hints** - `def add(a: float, b: float) -> float:`  
✅ **Docstrings** - Document your code  
✅ **Testing** - Make sure code works  
✅ **Imports** - Use code from other files  
✅ **Virtual Environments** - Isolated dependencies

---

## 🔧 Common Commands

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

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 👤 Author

**Ragul P** - [@ragulpalanisamy](https://github.com/ragulpalanisamy)

---

_Happy Learning! 🚀_
