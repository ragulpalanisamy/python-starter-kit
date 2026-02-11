# Python Type Checking, Type Casting & Type Hinting

## Table of Contents

1. [Type Checking](#type-checking)
2. [Type Casting](#type-casting)
3. [Type Casting Limitations](#limitations)
4. [Type Hinting](#type-hinting)
5. [Best Practices](#best-practices)

---

## Type Checking {#type-checking}

**Type checking** is the process of determining the data type of a variable at runtime.

### Methods for Type Checking

#### 1. Using `type()` Function

Returns the exact type of an object.

```python
user_id = '123'
age = 25
price = 99.99

print(type(user_id))  # <class 'str'>
print(type(age))      # <class 'int'>
print(type(price))    # <class 'float'>
```

#### 2. Using `isinstance()` Function (Recommended)

Checks if an object is an instance of a class or tuple of classes. This is the **preferred method** for type checking.

```python
user_id = '123'
age = 25

print(isinstance(user_id, str))  # True
print(isinstance(age, int))      # True
print(isinstance(age, (int, float)))  # True (checks multiple types)
```

**Why `isinstance()` is better:**

- Works with inheritance (subclasses)
- Can check multiple types at once
- More Pythonic and flexible

---

## Type Casting {#type-casting}

**Type casting** (or type conversion) is the process of converting a value from one data type to another.

### Common Type Conversions

#### String to Integer

```python
x = '10'
x_int = int(x)
print(x_int)  # 10
print(type(x_int))  # <class 'int'>
```

#### String to Float

```python
y = '10.5'
y_float = float(y)
print(y_float)  # 10.5
print(type(y_float))  # <class 'float'>
```

#### Integer to Float

```python
num = 42
num_float = float(num)
print(num_float)  # 42.0
```

#### Float to Integer (Truncates Decimal)

```python
pi = 3.14159
pi_int = int(pi)
print(pi_int)  # 3 (decimal part is removed, not rounded)
```

#### Number to String

```python
count = 100
count_str = str(count)
print(count_str)  # '100'
print(type(count_str))  # <class 'str'>
```

#### Boolean Conversions

```python
# Boolean to integer
print(int(True))   # 1
print(int(False))  # 0

# Integer to boolean (0 is False, non-zero is True)
print(bool(0))     # False
print(bool(1))     # True
print(bool(42))    # True
print(bool(-5))    # True
```

#### Collection Conversions

```python
# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3)

# String to list
text = "hello"
text_list = list(text)
print(text_list)  # ['h', 'e', 'l', 'l', 'o']

# List to set (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3]
unique = set(numbers)
print(unique)  # {1, 2, 3}
```

---

## Type Casting Limitations {#limitations}

Not all type conversions are possible. Here are common scenarios that will **fail**:

### ❌ String Float to Integer (Direct)

```python
z = '10.5'
# int(z)  # ❌ ValueError: invalid literal for int() with base 10: '10.5'

# ✅ Solution: Convert to float first, then to int
z_int = int(float(z))
print(z_int)  # 10
```

### ❌ Non-Numeric String to Number

```python
a = 'hello'
# int(a)  # ❌ ValueError: invalid literal for int() with base 10: 'hello'
```

### ❌ Empty String to Number

```python
b = ''
# int(b)  # ❌ ValueError: invalid literal for int() with base 10: ''
```

### ❌ None to Number

```python
c = None
# int(c)  # ❌ TypeError: int() argument must be a string or a number, not 'NoneType'
```

### Safe Type Casting with Error Handling

```python
def safe_int(value, default=0):
    """Safely convert to int, return default if conversion fails"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Usage
print(safe_int('42'))      # 42
print(safe_int('hello'))   # 0 (default)
print(safe_int(None))      # 0 (default)
print(safe_int('10.5'))    # ValueError, returns 0
```

---

## Type Hinting {#type-hinting}

**Type hinting** (introduced in Python 3.5+) allows you to specify the expected data types of variables, function parameters, and return values. This improves code readability and enables better IDE support.

> **Note:** Type hints are **not enforced** at runtime. They are primarily for documentation and static type checkers like `mypy`.

### Function Type Hints

```python
def greet(name: str) -> str:
    """Function with type hints"""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Add two integers"""
    return a + b

def calculate_price(quantity: int, price: float) -> float:
    """Calculate total price"""
    return quantity * price
```

### Variable Type Hints (Python 3.6+)

```python
username: str = "ragul-143"
age: int = 25
balance: float = 1000.50
is_active: bool = True
tags: list[str] = ["python", "coding", "learning"]
```

### Advanced Type Hints

```python
from typing import Optional, Union, List, Dict, Tuple

# Optional (can be None)
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Ragul"
    return None

# Union (multiple possible types)
def process_id(id_value: Union[int, str]) -> str:
    return str(id_value)

# Complex types
def get_user_data() -> Dict[str, Union[str, int]]:
    return {"name": "Ragul", "age": 25}

# List with specific type
def get_scores() -> List[int]:
    return [95, 87, 92]

# Tuple with specific types
def get_coordinates() -> Tuple[float, float]:
    return (12.9716, 77.5946)
```

---

## Best Practices {#best-practices}

### 1. Use `isinstance()` for Type Checking

```python
# ✅ GOOD
if isinstance(value, str):
    print("It's a string")

# ❌ AVOID
if type(value) == str:
    print("It's a string")
```

### 2. Handle Type Conversion Errors

```python
# ✅ GOOD - Safe conversion
try:
    age = int(user_input)
except ValueError:
    age = 0
    print("Invalid input, using default")

# ❌ BAD - No error handling
age = int(user_input)  # Can crash if user_input is not a valid number
```

### 3. Use Type Hints for Better Code Documentation

```python
# ✅ GOOD - Clear expectations
def calculate_discount(price: float, discount_percent: int) -> float:
    return price * (1 - discount_percent / 100)

# ❌ LESS CLEAR - No type information
def calculate_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)
```

### 4. Validate Before Casting

```python
# ✅ GOOD - Validate first
user_input = "42"
if user_input.isdigit():
    number = int(user_input)
else:
    print("Invalid number")

# String methods for validation
text = "hello"
print(text.isalpha())   # True (all alphabetic)
print(text.isdigit())   # False
print(text.isalnum())   # True (alphanumeric)
```

### 5. Be Aware of Implicit Conversions

```python
# Python automatically converts types in some operations
result = 5 + 2.5  # int + float = float
print(result)      # 7.5
print(type(result))  # <class 'float'>

# String concatenation requires explicit conversion
age = 25
# message = "Age: " + age  # ❌ TypeError
message = "Age: " + str(age)  # ✅ Correct
```

---

## Summary

| Concept           | Purpose                          | Example                           |
| ----------------- | -------------------------------- | --------------------------------- |
| **Type Checking** | Determine the type of a variable | `isinstance(x, int)`              |
| **Type Casting**  | Convert between types            | `int('42')`, `str(100)`           |
| **Type Hinting**  | Document expected types          | `def add(a: int, b: int) -> int:` |

**Key Takeaways:**

- Use `isinstance()` for type checking, not `type()`
- Always handle potential `ValueError` and `TypeError` when casting
- Type hints improve code readability but are not enforced at runtime
- Not all type conversions are possible (e.g., `'hello'` to `int`)
- Validate input before casting to avoid runtime errors

📁 See: [index.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/type-check-casting/index.py) for complete examples
