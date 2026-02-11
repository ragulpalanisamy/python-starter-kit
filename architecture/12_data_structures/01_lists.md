# Python Lists

Lists are ordered, mutable collections that can store multiple items.

## 1. List Basics

```python
fruits = ["apple", "banana", "mango"]
fruits[0]    # 'apple'
fruits[-1]   # 'mango'
```

## 2. List Methods

| Method         | Description                 |
| -------------- | --------------------------- |
| `append(x)`    | Add to end                  |
| `insert(i, x)` | Insert at position          |
| `remove(x)`    | Remove first occurrence     |
| `pop()`        | Remove and return last item |

## 3. List Comprehensions

```python
squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
```

---

[⬅️ Back to Data Structures](./index.md)
