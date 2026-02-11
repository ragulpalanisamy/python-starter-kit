# Instance vs Class vs Static Methods

## 1. Instance Methods

- **Purpose:** Access or modify object state.
- **Access:** Can access `self`.

```python
def method(self): pass
```

## 2. Class Methods

- **Purpose:** Access or modify class state.
- **Access:** Can access `cls`.
- **Decorator:** `@classmethod`

```python
@classmethod
def method(cls): pass
```

## 3. Static Methods

- **Purpose:** Utility methods that don't need class or object state.
- **Access:** No access to `self` or `cls`.
- **Decorator:** `@staticmethod`

```python
@staticmethod
def method(): pass
```

---

[⬅️ Back to OOP Home](./index.md)
