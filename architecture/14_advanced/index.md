# 🛠️ Advanced Python Concepts

These are concepts that make Python "Pythonic" and powerful.

## 1. Decorators (@)

Think of decorators as **Higher-Order Functions** or **Middleware** for a single function. They allow you to wrap a function to add behavior before or after it runs.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def say_hello():
    print("Hello!")
```

## 2. Context Managers (`with`)

Used for resource management (like open files or DB connections). It automatically handles "setup" and "teardown" (like `try...finally`).

```python
with open("data.txt", "w") as f:
    f.write("Hello")
# File is automatically closed here!
```

## 3. Dunder Methods (Double Under)

Methods like `__init__`, `__str__`, or `__add__`. They allow your custom objects to hook into native Python operations.

- `__init__`: The constructor.
- `__str__`: Like `toString()` in JS.
- `__len__`: Allows your object to work with `len(obj)`.

---

[⬅️ Back to Learning Path](../index.md)
