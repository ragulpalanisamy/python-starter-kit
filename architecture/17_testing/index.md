# PyTest Basics

Testing ensures your code works as expected.

## 1. Installation

```bash
pip install pytest
```

## 2. Writing a simple test

File: `test_math.py` (Must start with `test_`)

```python
def test_add():
    assert 1 + 1 == 2
```

## 3. Running tests

```bash
pytest
```

## Key Features

- **Assertions:** Use standard `assert` statements.
- **Fixtures:** Setup and teardown code.
- **Parametrization:** Run tests with multiple inputs.

---

[⬅️ Back to Learning Path](../index.md)
