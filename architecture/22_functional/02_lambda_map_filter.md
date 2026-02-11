# Lambda, Map, Filter, Reduce

## 1. Lambda Functions

Anonymous, one-line functions.

```python
square = lambda x: x * x
```

## 2. Map

Apply a function to all items in an iterable.

```python
nums = [1, 2, 3]
squared = list(map(lambda x: x*x, nums)) # [1, 4, 9]
```

## 3. Filter

Filter items in an iterable based on a condition.

```python
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) # [2, 4]
```

## 4. Reduce

Reduce an iterable to a single value by applying a function cumulatively.

```python
from functools import reduce
total = reduce(lambda x, y: x + y, [1, 2, 3, 4]) # 10
```

---

[⬅️ Back to Functional Home](./index.md)
