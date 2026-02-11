# Generators & yield

Generators allow you to declare a function that behaves like an iterator.

## 1. Using yield

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

gen = count_up_to(5)
for num in gen:
    print(num)
```

## 2. Why use Generators?

- **Memory Efficient:** They don't store the entire list in memory.
- **Lazy Evaluation:** Values are generated on the fly.

---

[⬅️ Back to Functional Home](./index.md)
