# Polymorphism

The ability to take many forms. Different classes can have the same method names.

```python
class Cat:
    def sound(self): return "Meow"

class Dog:
    def sound(self): return "Woof"

def make_sound(animal):
    print(animal.sound())
```

---

[⬅️ Back to OOP Home](./index.md)
