# Advanced Functional Patterns

## 1. Function Composition

The process of combining two or more functions to produce a new function.

```python
def add1(x): return x + 1
def square(x): return x * x

# (add1 . square)(x) = add1(square(x))
result = add1(square(5)) # 26
```

## 2. Callback Functions

Functions passed as arguments to other functions to be executed later.

## 3. Recursive Functions

Functions that call themselves.

```python
def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)
```

---

[⬅️ Back to Functional Home](./index.md)
