# Closures & Partial Functions

## 1. Closures

A function that references variables from its enclosing scope even after the enclosing scope has finished executing.

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(10)) # 30
```

## 2. Partial Functions

Fix a certain number of arguments of a function and generate a new function.

```python
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5)) # 10
```

---

[⬅️ Back to Functional Home](./index.md)
