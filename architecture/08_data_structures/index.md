# Python Lists - Complete Guide

## Table of Contents

1. [List Basics](#basics)
2. [List Methods](#methods)
3. [List Operations](#operations)
4. [Practical Examples](#practical)

---

## List Basics {#basics}

Lists are ordered, mutable collections that can store multiple items.

### Creating Lists

```python
# Empty list
empty = []

# List with values
numbers = [1, 2, 3, 4, 5]

# Mixed data types
mixed = [1, "hello", 3.14, True]

# Using list() constructor
from_range = list(range(5))      # [0, 1, 2, 3, 4]
from_string = list("Python")     # ['P', 'y', 't', 'h', 'o', 'n']
```

### Accessing Elements

```python
fruits = ["apple", "banana", "mango"]

# Indexing (0-based)
fruits[0]    # 'apple' (first)
fruits[-1]   # 'mango' (last)
fruits[1]    # 'banana' (second)
```

### Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[0:5]   # [0, 1, 2, 3, 4]
numbers[5:]    # [5, 6, 7, 8, 9]
numbers[:5]    # [0, 1, 2, 3, 4]
numbers[::2]   # [0, 2, 4, 6, 8] (every 2nd)
numbers[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)
```

### Membership

```python
fruits = ["apple", "banana", "mango"]

"apple" in fruits      # True
"orange" in fruits     # False
"banana" not in fruits # False
```

### List Operations

| Operation     | Example           | Result               |
| ------------- | ----------------- | -------------------- |
| Concatenation | `[1, 2] + [3, 4]` | `[1, 2, 3, 4]`       |
| Repetition    | `[0, 1] * 3`      | `[0, 1, 0, 1, 0, 1]` |
| Length        | `len([1, 2, 3])`  | `3`                  |

📁 [basics.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/lists/basics.py)

---

## List Methods {#methods}

### Adding Elements

| Method             | Description        | Example                   |
| ------------------ | ------------------ | ------------------------- |
| `append(x)`        | Add item to end    | `list.append(5)`          |
| `insert(i, x)`     | Insert at position | `list.insert(0, 'first')` |
| `extend(iterable)` | Add multiple items | `list.extend([4, 5, 6])`  |

```python
fruits = ["apple"]

fruits.append("banana")              # ["apple", "banana"]
fruits.insert(0, "mango")            # ["mango", "apple", "banana"]
fruits.extend(["orange", "grape"])   # ["mango", "apple", "banana", "orange", "grape"]
```

### Removing Elements

| Method      | Description             | Example                       |
| ----------- | ----------------------- | ----------------------------- |
| `remove(x)` | Remove first occurrence | `list.remove('apple')`        |
| `pop([i])`  | Remove and return item  | `list.pop()` or `list.pop(0)` |
| `clear()`   | Remove all items        | `list.clear()`                |

```python
fruits = ["apple", "banana", "mango"]

fruits.remove("banana")   # ["apple", "mango"]
last = fruits.pop()       # last = "mango", fruits = ["apple"]
fruits.clear()            # []
```

### Finding & Counting

| Method     | Description       | Example               |
| ---------- | ----------------- | --------------------- |
| `index(x)` | Find position     | `list.index('apple')` |
| `count(x)` | Count occurrences | `list.count(2)`       |

```python
fruits = ["apple", "banana", "apple"]

fruits.index("banana")    # 1
fruits.count("apple")     # 2
```

### Sorting & Reversing

| Method      | Description        | In-place? |
| ----------- | ------------------ | --------- |
| `sort()`    | Sort list          | Yes       |
| `sorted()`  | Return sorted copy | No        |
| `reverse()` | Reverse list       | Yes       |

```python
numbers = [5, 2, 8, 1, 9]

# In-place sorting
numbers.sort()              # [1, 2, 5, 8, 9]
numbers.sort(reverse=True)  # [9, 8, 5, 2, 1]

# Return sorted copy
numbers = [5, 2, 8, 1, 9]
sorted_nums = sorted(numbers)  # sorted_nums = [1, 2, 5, 8, 9]
                                # numbers unchanged

# Reverse
numbers.reverse()  # [9, 1, 8, 2, 5]
```

### Copying

```python
original = [1, 2, 3]

# Shallow copy
copy = original.copy()
copy = original[:]
copy = list(original)
```

📁 [methods.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/lists/methods.py)

---

## List Operations {#operations}

### List Comprehension

Create lists in a concise way.

```python
# Basic
squares = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Transform
fruits = ["apple", "banana"]
upper = [f.upper() for f in fruits]  # ["APPLE", "BANANA"]

# Nested
pairs = [(x, y) for x in range(2) for y in range(2)]
# [(0, 0), (0, 1), (1, 0), (1, 1)]
```

### Iterating

```python
fruits = ["apple", "banana", "mango"]

# Simple iteration
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# With custom start
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

### Unpacking

```python
# Basic
numbers = [1, 2, 3]
a, b, c = numbers  # a=1, b=2, c=3

# Extended
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
# first=1, middle=[2, 3, 4], last=5
```

### Nested Lists (2D Lists)

```python
# Create matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
matrix[0][0]  # 1
matrix[1][2]  # 6

# Flatten
flat = [item for row in matrix for item in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Min/Max/Sum

```python
numbers = [45, 23, 89, 12, 67]

min(numbers)                    # 12
max(numbers)                    # 89
sum(numbers)                    # 236
sum(numbers) / len(numbers)     # 47.2 (average)
```

### Filtering

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Using comprehension (preferred)
evens = [x for x in numbers if x % 2 == 0]
```

### Mapping

```python
numbers = [1, 2, 3, 4, 5]

# Using map()
squared = list(map(lambda x: x ** 2, numbers))

# Using comprehension (preferred)
squared = [x ** 2 for x in numbers]
```

### Zipping

Combine multiple lists.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Combine
combined = list(zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Iterate
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

### Removing Duplicates

```python
numbers = [1, 2, 3, 2, 4, 3, 5, 1]

# Using set (loses order)
unique = list(set(numbers))

# Preserving order
unique = list(dict.fromkeys(numbers))
# [1, 2, 3, 4, 5]
```

📁 [operations.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/lists/operations.py)

---

## Practical Examples {#practical}

### 1. Shopping Cart

```python
cart = []
cart.append({"item": "Apple", "price": 50, "quantity": 3})
cart.append({"item": "Banana", "price": 30, "quantity": 5})

total = sum(item["price"] * item["quantity"] for item in cart)
```

### 2. Grade Management

```python
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92}
]

# Sort by marks
sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)

# Find top scorer
top = max(students, key=lambda x: x["marks"])

# Average
avg = sum(s["marks"] for s in students) / len(students)
```

### 3. To-Do List

```python
todos = [
    {"task": "Buy groceries", "done": False},
    {"task": "Complete assignment", "done": True}
]

# Display
for i, todo in enumerate(todos, 1):
    status = "✅" if todo["done"] else "❌"
    print(f"{i}. {status} {todo['task']}")
```

### 4. Contact List

```python
contacts = [
    {"name": "Alice", "phone": "1234567890"},
    {"name": "Bob", "phone": "9876543210"}
]

# Search
search = "Alice"
found = [c for c in contacts if c["name"].lower() == search.lower()]
```

### 5. Inventory Management

```python
inventory = [
    {"product": "Laptop", "stock": 5},
    {"product": "Mouse", "stock": 0}
]

# Low stock alert
low_stock = [item for item in inventory if 0 < item["stock"] < 10]
```

### 6. Number Analysis

```python
numbers = [12, 45, 23, 67, 34, 89]

evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]
above_50 = [n for n in numbers if n > 50]
```

### 7. Word Frequency

```python
text = "hello world hello python"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
```

### 8. Remove Items

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Remove all evens
numbers = [n for n in numbers if n % 2 != 0]
```

### 9. Merge and Sort

```python
list1 = [3, 1, 4]
list2 = [9, 2, 6]

merged = list1 + list2
merged.sort()

unique_sorted = sorted(list(set(merged)))
```

### 10. Matrix Operations

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Sum all
total = sum(sum(row) for row in matrix)

# Diagonal
diagonal = [matrix[i][i] for i in range(len(matrix))]

# Transpose
transpose = [[matrix[j][i] for j in range(len(matrix))]
             for i in range(len(matrix[0]))]
```

📁 [practical.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/lists/practical.py)

---

## Quick Reference

### Common Operations

| Operation | Syntax                 | Example            |
| --------- | ---------------------- | ------------------ |
| Create    | `[]` or `list()`       | `nums = [1, 2, 3]` |
| Access    | `list[index]`          | `nums[0]`          |
| Slice     | `list[start:end]`      | `nums[1:3]`        |
| Add       | `append()`, `insert()` | `nums.append(4)`   |
| Remove    | `remove()`, `pop()`    | `nums.pop()`       |
| Sort      | `sort()`, `sorted()`   | `nums.sort()`      |
| Length    | `len()`                | `len(nums)`        |
| Check     | `in`                   | `1 in nums`        |

### List Methods Summary

| Method         | Modifies List? | Returns      |
| -------------- | -------------- | ------------ |
| `append(x)`    | Yes            | None         |
| `insert(i, x)` | Yes            | None         |
| `extend(list)` | Yes            | None         |
| `remove(x)`    | Yes            | None         |
| `pop([i])`     | Yes            | Removed item |
| `clear()`      | Yes            | None         |
| `index(x)`     | No             | Index        |
| `count(x)`     | No             | Count        |
| `sort()`       | Yes            | None         |
| `reverse()`    | Yes            | None         |
| `copy()`       | No             | New list     |

---

## Best Practices

### ✅ Do

1. **Use list comprehensions** for simple transformations
2. **Use meaningful names** - `students` not `s`
3. **Check before accessing** - avoid index errors
4. **Use `in` for membership** - cleaner than loops
5. **Copy when needed** - avoid unintended modifications

### ❌ Don't

```python
# ❌ BAD - Modifying list while iterating
for item in items:
    items.remove(item)  # Can skip items

# ✅ GOOD - Create new list
items = [item for item in items if condition]

# ❌ BAD - Unnecessary loop
result = []
for x in numbers:
    result.append(x ** 2)

# ✅ GOOD - Use comprehension
result = [x ** 2 for x in numbers]
```

---

## Summary

| Concept           | Purpose                     | Example                   |
| ----------------- | --------------------------- | ------------------------- |
| **List**          | Ordered, mutable collection | `[1, 2, 3]`               |
| **Indexing**      | Access elements             | `list[0]`                 |
| **Slicing**       | Get subset                  | `list[1:3]`               |
| **append()**      | Add to end                  | `list.append(4)`          |
| **extend()**      | Add multiple                | `list.extend([4, 5])`     |
| **remove()**      | Remove by value             | `list.remove(2)`          |
| **pop()**         | Remove by index             | `list.pop(0)`             |
| **Comprehension** | Create lists                | `[x*2 for x in range(5)]` |

**Remember:**

- Lists are **mutable** (can be changed)
- Indexing starts at **0**
- Use **comprehensions** for concise code
- **Copy** lists when needed to avoid side effects
- Lists can contain **any data type**
