# Encapsulation & Access Specifiers

Encapsulation restricts direct access to data and methods.

## Access Specifiers

| Type          | Syntax        | Description                            |
| ------------- | ------------- | -------------------------------------- |
| **Public**    | `self.name`   | Accessible from anywhere               |
| **Protected** | `self._name`  | Accessible within class and subclasses |
| **Private**   | `self.__name` | Accessible ONLY within the class       |

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance # Private
```

---

[⬅️ Back to OOP Home](./index.md)
