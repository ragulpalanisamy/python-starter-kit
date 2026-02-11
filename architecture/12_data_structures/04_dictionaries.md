# Python Dictionaries

Dictionaries store data in **key-value pairs**.

## 1. Dictionary Basics

```python
user = {
    "name": "Ragul",
    "age": 25,
    "city": "Chennai"
}
```

## 2. Accessing Data

```python
print(user["name"]) # Ragul
print(user.get("email", "Not Found")) # Safe access
```

## 3. Key Features

- **Key-Value:** Data is organized by keys, not indices.
- **Mutable:** You can change values and add new keys.
- **Ordered:** As of Python 3.7+, dictionaries preserve insertion order.

---

[⬅️ Back to Data Structures](./index.md)
