# Functional Programming Basics

Functional programming is a paradigm where programs are constructed by applying and composing functions.

## 1. Pure vs Impure Functions

- **Pure Function:** Always produces the same output for the same input and has no side effects (doesn't modify external variables).
- **Impure Function:** Can produce different outputs for the same input or has side effects (e.g., printing to console, modifying a global variable).

## 2. Higher-Order Functions

A function that takes another function as an argument or returns a function as a result.

```python
def apply(func, val):
    return func(val)

print(apply(abs, -5)) # 5
```

---

[⬅️ Back to Functional Home](./index.md)
