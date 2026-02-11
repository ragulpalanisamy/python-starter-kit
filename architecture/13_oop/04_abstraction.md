# Abstraction

Hiding complex implementation details and showing only the necessary features.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass
```

## Why use Abstraction?

- Reduces complexity.
- Defines a common interface for a group of subclasses.

---

[⬅️ Back to OOP Home](./index.md)
