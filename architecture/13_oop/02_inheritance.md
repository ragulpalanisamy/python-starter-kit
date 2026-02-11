# Inheritance

Child classes inherit features from parent classes.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")
```

## Key Points

- Use `super()` to call the parent class methods.
- Supports code reuse and "is-a" relationships.

---

[⬅️ Back to OOP Home](./index.md)
