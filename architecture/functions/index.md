# Python Functions - Complete Guide

## Table of Contents

1. [Function Basics](#basics)
2. [Function Arguments](#arguments)
3. [Scope & Variables](#scope)
4. [Lambda & Special Functions](#lambda)
5. [Practical Examples](#practical)

---

## Function Basics {#basics}

Functions are reusable blocks of code that perform specific tasks.

### Simple Function

```python
def greet():
    """Function without parameters"""
    print("Hello, World!")

greet()  # Call the function
```

### Function with Parameters

```python
def greet_user(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

greet_user("Ragul")
```

### Function with Return Value

```python
def multiply(a, b):
    """Function that returns a value"""
    return a * b

result = multiply(5, 3)  # result = 15
```

### Multiple Return Values

```python
def get_user_info():
    """Return multiple values as tuple"""
    return "Ragul", 25, "Chennai"

name, age, city = get_user_info()
```

### Default Parameters

```python
def greet(name, title="Mr."):
    """Parameter with default value"""
    print(f"Hello, {title} {name}!")

greet("Ragul")           # Uses default "Mr."
greet("Ragul", "Dr.")    # Overrides default
```

### Docstring (Documentation)

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length (float): Length of rectangle
        width (float): Width of rectangle

    Returns:
        float: Area of rectangle
    """
    return length * width
```

📁 [basics.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/functions/basics.py)

---

## Function Arguments {#arguments}

Different ways to pass arguments to functions.

### Positional Arguments

```python
def create_profile(name, age, city):
    print(f"{name}, {age}, {city}")

create_profile("Ragul", 25, "Chennai")  # Order matters
```

### Keyword Arguments

```python
create_profile(city="Chennai", name="Ragul", age=25)  # Order doesn't matter
```

### Mixed Arguments

```python
create_profile("Ragul", age=25, city="Chennai")  # Positional first, then keyword
```

### Default Arguments

```python
def create_user(name, role="User", active=True):
    print(f"{name}: {role}, Active: {active}")

create_user("Ragul")                    # Uses defaults
create_user("Alice", "Admin")           # Overrides role
create_user("Bob", active=False)        # Overrides active
```

### \*args - Variable Positional Arguments

Accept any number of positional arguments.

```python
def sum_all(*numbers):
    """Accept any number of arguments"""
    return sum(numbers)

sum_all(1, 2, 3)           # 6
sum_all(10, 20, 30, 40)    # 100
```

### \*\*kwargs - Variable Keyword Arguments

Accept any number of keyword arguments.

```python
def display_info(**info):
    """Accept any number of keyword arguments"""
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Ragul", age=25, city="Chennai")
```

### Combining All Types

```python
def create_order(item, quantity, *extras, discount=0, **details):
    """
    - item, quantity: positional
    - *extras: variable positional
    - discount: keyword with default
    - **details: variable keyword
    """
    print(f"Item: {item}, Qty: {quantity}")
    print(f"Extras: {extras}")
    print(f"Discount: {discount}%")
    print(f"Details: {details}")

create_order("Pizza", 2, "Cheese", "Olives", discount=10, delivery="Express")
```

### Argument Order

**Must follow this order:**

1. Positional arguments
2. \*args
3. Keyword arguments
4. \*\*kwargs

📁 [arguments.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/functions/arguments.py)

---

## Scope & Variables {#scope}

Variable visibility and lifetime in functions.

### Local Variables

Variables inside functions are **local** (only accessible inside).

```python
def calculate():
    x = 10  # Local variable
    print(x)

calculate()
# print(x)  # ❌ Error: x not defined outside
```

### Global Variables

Variables outside functions are **global** (accessible everywhere).

```python
counter = 0  # Global variable

def increment():
    print(counter)  # Can read global

increment()
```

### Modifying Global Variables

Use `global` keyword to modify global variables.

```python
total = 0

def add_to_total(amount):
    global total  # Declare as global
    total += amount

add_to_total(10)
print(total)  # 10
```

### Nonlocal Variables

Use `nonlocal` in nested functions to access enclosing variables.

```python
def outer():
    count = 0

    def inner():
        nonlocal count  # Access outer function's variable
        count += 1
        print(count)

    inner()  # 1
    inner()  # 2
```

### Return vs Print

| `return`                   | `print`                       |
| -------------------------- | ----------------------------- |
| Sends value back to caller | Displays value on screen      |
| Can be used in expressions | Cannot be used in expressions |
| Function ends after return | Function continues            |

```python
def return_sum(a, b):
    return a + b

def print_sum(a, b):
    print(a + b)

result1 = return_sum(5, 3)   # result1 = 8
result2 = print_sum(5, 3)    # Prints 8, result2 = None
```

📁 [scope.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/functions/scope.py)

---

## Lambda & Special Functions {#lambda}

### Lambda Functions

Anonymous one-line functions.

**Syntax:** `lambda parameters: expression`

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

# Multiple parameters
add = lambda a, b: a + b
```

### Lambda with Sorting

```python
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20}
]

# Sort by age
sorted_students = sorted(students, key=lambda x: x["age"])
```

### map() - Apply Function to All Items

```python
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]
```

### filter() - Filter Items

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]
```

### reduce() - Reduce to Single Value

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Calculate product
product = reduce(lambda x, y: x * y, numbers)
# 120 (1*2*3*4*5)
```

### Recursive Functions

Functions that call themselves.

```python
def factorial(n):
    """Calculate n! using recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

factorial(5)  # 120 (5*4*3*2*1)
```

```python
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

📁 [lambda-special.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/functions/lambda-special.py)

---

## Practical Examples {#practical}

### 1. Email Validator

```python
def is_valid_email(email):
    """Check if email is valid"""
    return "@" in email and "." in email.split("@")[1]

is_valid_email("user@example.com")  # True
```

### 2. Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
```

### 3. Password Strength Checker

```python
def check_password_strength(password):
    """Check password strength"""
    score = 0
    if len(password) >= 8: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(not c.isalnum() for c in password): score += 1

    strengths = ["Very Weak", "Weak", "Fair", "Good", "Strong"]
    return strengths[score - 1] if score > 0 else "Very Weak"
```

### 4. Discount Calculator

```python
def calculate_discount(price, discount_percent=0):
    """Calculate final price after discount"""
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price, discount_amount
```

### 5. Prime Number Finder

```python
def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(limit):
    """Get all primes up to limit"""
    return [n for n in range(2, limit + 1) if is_prime(n)]
```

### 6. String Formatter

```python
def format_name(first, last, title=""):
    """Format person's name"""
    if title:
        return f"{title} {first} {last}"
    return f"{first} {last}"

def format_phone(number):
    """Format phone number as (XXX) XXX-XXXX"""
    digits = ''.join(filter(str.isdigit, number))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return number
```

### 7. List Statistics

```python
def get_stats(numbers):
    """Calculate statistics"""
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }
```

### 8. Grade Calculator

```python
def calculate_grade(marks):
    """Calculate grade based on marks"""
    if marks >= 90: return "A"
    elif marks >= 80: return "B"
    elif marks >= 70: return "C"
    elif marks >= 60: return "D"
    else: return "F"
```

### 9. Shopping Cart

```python
def add_to_cart(cart, item, price, quantity=1):
    """Add item to cart"""
    cart[item] = {"price": price, "quantity": quantity}
    return cart

def calculate_total(cart):
    """Calculate total"""
    return sum(item["price"] * item["quantity"]
               for item in cart.values())
```

### 10. Text Analyzer

```python
def analyze_text(text):
    """Analyze text statistics"""
    words = text.split()
    return {
        "characters": len(text),
        "words": len(words),
        "sentences": text.count('.') + text.count('!') + text.count('?'),
        "vowels": sum(1 for c in text.lower() if c in 'aeiou')
    }
```

📁 [practical.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/functions/practical.py)

---

## Quick Reference

### Function Definition

```python
def function_name(parameters):
    """Docstring"""
    # Function body
    return value
```

### Argument Types

| Type       | Syntax               | Example                  |
| ---------- | -------------------- | ------------------------ |
| Positional | `func(a, b)`         | `greet("Ragul", 25)`     |
| Keyword    | `func(name=value)`   | `greet(name="Ragul")`    |
| Default    | `def func(a=10)`     | `def greet(title="Mr.")` |
| \*args     | `def func(*args)`    | `def sum_all(*nums)`     |
| \*\*kwargs | `def func(**kwargs)` | `def info(**data)`       |

### Special Functions

| Function   | Purpose           | Example              |
| ---------- | ----------------- | -------------------- |
| `lambda`   | One-line function | `lambda x: x ** 2`   |
| `map()`    | Apply to all      | `map(func, list)`    |
| `filter()` | Filter items      | `filter(func, list)` |
| `reduce()` | Reduce to one     | `reduce(func, list)` |

---

## Best Practices

### ✅ Do

1. **Use descriptive names** - `calculate_total()` not `calc()`
2. **Write docstrings** - Document what function does
3. **Keep functions small** - One task per function
4. **Use type hints** - `def add(a: int, b: int) -> int:`
5. **Return values** - Don't just print

### ❌ Don't

```python
# ❌ BAD - Too many responsibilities
def process_user(name, email, age, city, role):
    # Validate
    # Save to database
    # Send email
    # Log activity
    pass

# ✅ GOOD - Separate functions
def validate_user(data): pass
def save_user(data): pass
def send_welcome_email(email): pass
def log_activity(action): pass
```

```python
# ❌ BAD - Modifying global without global keyword
count = 0
def increment():
    count += 1  # Error!

# ✅ GOOD - Use global or return
def increment(count):
    return count + 1
```

---

## Summary

| Concept          | Purpose               | Example                 |
| ---------------- | --------------------- | ----------------------- |
| **Function**     | Reusable code block   | `def greet(): ...`      |
| **Parameters**   | Input to function     | `def add(a, b): ...`    |
| **Return**       | Output from function  | `return a + b`          |
| **Default args** | Optional parameters   | `def func(a=10): ...`   |
| **\*args**       | Variable positional   | `def sum(*nums): ...`   |
| **kwargs**       | Variable keyword      | `def info(**data): ...` |
| **Lambda**       | Anonymous function    | `lambda x: x ** 2`      |
| **Recursion**    | Function calls itself | `factorial(n-1)`        |

**Remember:**

- Functions make code **reusable** and **organized**
- Use **return** to send values back
- **Docstrings** document your functions
- **Lambda** for simple one-line functions
- Keep functions **small** and **focused**
