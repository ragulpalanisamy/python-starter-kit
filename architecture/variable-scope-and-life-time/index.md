# Python Variable Scope and Lifetime

## Table of Contents

1. [LEGB Rule - Variable Scope Resolution](#legb-rule)
2. [Variable Lifetime](#variable-lifetime)
3. [Mutability vs Immutability](#mutability)
4. [Best Practices](#best-practices)

---

## LEGB Rule - Variable Scope Resolution {#legb-rule}

Python uses the **LEGB rule** to resolve variable names. When you reference a variable, Python searches in this order:

1. **L**ocal
2. **E**nclosing
3. **G**lobal
4. **B**uilt-in

### L - Local Scope

Variables defined **inside a function** are in the local scope.

**Characteristics:**

- Only accessible within the function where they're defined
- Created when the function is called
- Destroyed when the function exits
- Each function call creates a new local scope

**Example:**

```python
def order_food():
    food = 'Ice Briyani'  # Local variable
    print(f'I want to order {food}')

order_food()  # Output: I want to order Ice Briyani
# print(food)  # ❌ NameError: name 'food' is not defined
```

📁 See: [local-variable.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/variable-scope/local-variable.py)

---

### E - Enclosing Scope

Variables defined in an **outer (enclosing) function** that are accessible to **inner (nested) functions**.

**Characteristics:**

- Exists in nested function scenarios
- The inner function can access variables from the outer function
- Created when the outer function is called
- Destroyed when the outer function exits

**Example:**

```python
def cart():
    """Outer function"""
    discount = 10  # Enclosing variable

    def discount_price():
        """Inner function"""
        print(f'Discount price is {discount}')  # Accessing enclosing variable

    discount_price()

cart()  # Output: Discount price is 10
# print(discount)  # ❌ NameError: name 'discount' is not defined
```

📁 See: [enclosing-variable.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/variable-scope/enclosing-variable.py)

---

### G - Global Scope

Variables defined **at the module level** (outside all functions).

**Characteristics:**

- Accessible from anywhere in the module (including inside functions)
- Created when the module/script starts
- Destroyed when the program exits
- Can be modified inside functions using the `global` keyword

**Example:**

```python
user_id = "ragul-143"  # Global variable

def login():
    print(f'User {user_id} is logging in')

def home_page():
    print(f'Welcome to home page {user_id}')

login()      # Output: User ragul-143 is logging in
home_page()  # Output: Welcome to home page ragul-143
```

📁 See: [global-variable.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/variable-scope/global-variable.py)

---

### B - Built-in Scope

**Built-in names** provided by Python (functions, exceptions, constants).

**Characteristics:**

- Pre-defined by Python
- Always available without importing
- Accessible from anywhere
- Examples: `print()`, `len()`, `type()`, `True`, `False`, `None`, `Exception`, etc.

**Example:**

```python
# These are all built-in functions/constants
print(type(True))        # <class 'bool'>
print(len([1, 2, 3]))    # 3
print(isinstance(5, int)) # True
```

📁 See: [built-in.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/variable-scope/built-in.py)

---

### Complete LEGB Example

```python
# ordering food from swiggy

delivery_partner = "swiggy"  # Global variable

def order_food():
    food = "ice briyani"  # Enclosing variable

    def total_quantity():
        quantity = 2  # Local variable
        print(f'Ordering {quantity} {food} from {delivery_partner}')
        # Uses: Local (quantity), Enclosing (food), Global (delivery_partner)

    total_quantity()

order_food()  # Output: Ordering 2 ice briyani from swiggy

# Built-in example
print(__file__)  # Built-in variable
```

📁 See: [complete-work-around.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/variable-scope/complete-work-around.py)

---

## Variable Lifetime {#variable-lifetime}

**Lifetime** refers to how long a variable exists in memory.

| Scope         | Lifetime                                                                     |
| ------------- | ---------------------------------------------------------------------------- |
| **Local**     | Created when function is called, destroyed when function returns             |
| **Enclosing** | Created when outer function is called, destroyed when outer function returns |
| **Global**    | Created when module loads, destroyed when program exits                      |
| **Built-in**  | Exists for the entire duration of the Python interpreter session             |

**Example:**

```python
def calculate():
    x = 10  # Created here
    print(x)
    # x is destroyed when function returns

calculate()
# x no longer exists in memory
```

---

## Mutability vs Immutability {#mutability}

> **Note:** Mutability is **NOT** part of the LEGB scope rule. It's a separate concept about whether an object's value can be changed.

### Immutable Types

Objects whose **value cannot be changed** after creation. Modifying them creates a **new object**.

**Immutable types:**

- `int`, `float`, `complex`
- `str` (string)
- `tuple`
- `frozenset`
- `bool`
- `bytes`

**Example:**

```python
x = 10
print(id(x))  # Memory address: 140234567890

x = 20  # Creates a NEW object, doesn't modify the old one
print(id(x))  # Different memory address: 140234567920

# Strings are immutable
name = "Ragul"
# name[0] = "r"  # ❌ TypeError: 'str' object does not support item assignment
```

---

### Mutable Types

Objects whose **value can be changed** in-place without creating a new object.

**Mutable types:**

- `list`
- `dict`
- `set`
- `bytearray`

**Example:**

```python
numbers = [1, 2, 3]
print(id(numbers))  # Memory address: 140234567890

numbers.append(4)  # Modifies the SAME object
print(id(numbers))  # Same memory address: 140234567890
print(numbers)      # [1, 2, 3, 4]

# Dictionaries are mutable
person = {"name": "Ragul", "age": 25}
person["city"] = "Chennai"  # Modifies in-place
```

---

## Best Practices {#best-practices}

1. **Minimize global variables** - Use function parameters and return values instead
2. **Use descriptive names** - Make variable purpose clear from the name
3. **Prefer local scope** - Keep variables in the smallest scope necessary
4. **Be careful with mutable defaults** - Don't use mutable objects as default function arguments
5. **Use `global` and `nonlocal` sparingly** - They can make code harder to understand

**Example of mutable default pitfall:**

```python
# ❌ BAD - Mutable default argument
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['apple', 'banana'] - Unexpected!

# ✅ GOOD - Use None as default
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['banana'] - As expected!
```

---

## Summary

- **LEGB** = Scope resolution order (Local → Enclosing → Global → Built-in)
- **Lifetime** = How long a variable exists in memory
- **Mutability** = Whether an object's value can be changed in-place
- Understanding these concepts helps write cleaner, more predictable Python code
