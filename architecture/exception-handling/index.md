# Exception Handling - Simple Guide

## Table of Contents

1. [What are Exceptions?](#what-are-exceptions)
2. [Try-Except Basics](#try-except)
3. [Common Exceptions](#common-exceptions)
4. [Raising Exceptions](#raising)
5. [Custom Exceptions](#custom)
6. [Practical Examples](#practical)

---

## 🖼️ Visual Architecture

![Python Exception Handling Diagram](exception-handling.png)

## What are Exceptions? {#what-are-exceptions}

**Exception** = Error that occurs during program execution

### Without Exception Handling

```python
# ❌ Program crashes
result = 10 / 0  # ZeroDivisionError
print("This line never runs")
```

### With Exception Handling

```python
# ✅ Program continues
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
    result = None

print("Program continues running")
```

---

## Try-Except Basics {#try-except}

### Basic Structure

```python
try:
    # Code that might cause error
    result = 10 / 0
except ZeroDivisionError:
    # Handle the error
    print("Cannot divide by zero!")
```

### Multiple Exceptions

```python
try:
    result = int("abc")
except ValueError:
    print("Invalid value!")
except TypeError:
    print("Wrong type!")
```

### Catching Multiple Exceptions Together

```python
try:
    result = 10 / 0
except (ZeroDivisionError, TypeError) as e:
    print(f"Error: {e}")
```

### Try-Except-Else

**`else` block runs if NO exception occurs**

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Success! Result = {result}")
```

### Try-Except-Finally

**`finally` block ALWAYS runs (cleanup code)**

```python
try:
    file = open("file.txt", "w")
    file.write("Hello")
except Exception as e:
    print(f"Error: {e}")
finally:
    file.close()  # Always closes file
    print("Cleanup done")
```

### Complete Structure

```python
try:
    # Try to do something
    result = 10 / 2
except ZeroDivisionError:
    # Handle specific error
    print("Division by zero!")
except Exception as e:
    # Handle any other error
    print(f"Error: {e}")
else:
    # Runs if no error
    print(f"Success: {result}")
finally:
    # Always runs
    print("Cleanup")
```

---

## Common Exceptions {#common-exceptions}

| Exception           | When it Occurs     | Example               |
| ------------------- | ------------------ | --------------------- |
| `ZeroDivisionError` | Division by zero   | `10 / 0`              |
| `ValueError`        | Invalid value      | `int("abc")`          |
| `TypeError`         | Wrong type         | `"10" + 5`            |
| `IndexError`        | Invalid index      | `[1, 2][10]`          |
| `KeyError`          | Key not found      | `{"a": 1}["b"]`       |
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
| `AttributeError`    | Attribute missing  | `"text".append()`     |
| `NameError`         | Variable undefined | `print(x)`            |
| `ImportError`       | Module not found   | `import xyz`          |

### Examples

```python
# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ValueError
try:
    number = int("abc")
except ValueError:
    print("Invalid number!")

# TypeError
try:
    result = "10" + 5
except TypeError:
    print("Cannot add string and number!")

# IndexError
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Index out of range!")

# KeyError
try:
    user = {"name": "Ragul"}
    print(user["email"])
except KeyError:
    print("Key not found!")

# FileNotFoundError
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
```

📁 [common-exceptions.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/exception-handling/common-exceptions.py)

---

## Raising Exceptions {#raising}

### Using `raise`

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 120:
        raise ValueError("Age too high!")
    return True

try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")
```

### Re-raising Exceptions

```python
def process_data(data):
    try:
        result = int(data)
        return result
    except ValueError:
        print("Logging error...")
        raise  # Re-raise the same exception

try:
    process_data("abc")
except ValueError:
    print("Invalid data!")
```

### Assert Statements

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty!"
    return sum(numbers) / len(numbers)

try:
    avg = calculate_average([])
except AssertionError as e:
    print(f"Assertion failed: {e}")
```

📁 [raising-exceptions.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/exception-handling/raising-exceptions.py)

---

## Custom Exceptions {#custom}

Create your own exception types for specific errors.

### Basic Custom Exception

```python
class InsufficientFundsError(Exception):
    """Custom exception for banking"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ₹{amount}. Balance: ₹{self.balance}"
            )
        self.balance -= amount

account = BankAccount(1000)

try:
    account.withdraw(1500)
except InsufficientFundsError as e:
    print(f"Error: {e}")
```

### Custom Exception with Data

```python
class ValidationError(Exception):
    """Custom validation exception"""

    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

def validate_user(user):
    if not user.get("email"):
        raise ValidationError("email", "Email is required")
    if "@" not in user["email"]:
        raise ValidationError("email", "Invalid email format")

try:
    validate_user({"email": "invalid"})
except ValidationError as e:
    print(f"Validation failed - {e.field}: {e.message}")
```

---

## Practical Examples {#practical}

### Example 1: User Input Validation

```python
def get_positive_number():
    """Get positive number from user"""
    while True:
        try:
            num = int(input("Enter positive number: "))
            if num <= 0:
                raise ValueError("Number must be positive")
            return num
        except ValueError as e:
            print(f"Invalid input: {e}")
```

### Example 2: File Operations

```python
def read_file_safely(filename):
    """Read file with error handling"""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Permission denied")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

content = read_file_safely("data.txt")
```

### Example 3: API Request Simulation

```python
class APIError(Exception):
    """Custom API exception"""
    pass

def fetch_user(user_id):
    """Fetch user data"""
    try:
        if user_id <= 0:
            raise ValueError("Invalid user ID")
        if user_id > 100:
            raise APIError("User not found")

        return {"id": user_id, "name": f"User{user_id}"}

    except ValueError as e:
        print(f"Validation error: {e}")
        return None
    except APIError as e:
        print(f"API error: {e}")
        return None

user = fetch_user(50)
```

### Example 4: Calculator

```python
class Calculator:
    @staticmethod
    def divide(a, b):
        try:
            if not isinstance(a, (int, float)):
                raise TypeError("First argument must be number")
            if not isinstance(b, (int, float)):
                raise TypeError("Second argument must be number")
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        except (TypeError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            return None

result = Calculator.divide(10, 2)  # 5.0
result = Calculator.divide(10, 0)  # Error: Cannot divide by zero
```

### Example 5: Retry Mechanism

```python
def retry_operation(func, max_attempts=3):
    """Retry function on failure"""
    for attempt in range(1, max_attempts + 1):
        try:
            result = func()
            print(f"Success on attempt {attempt}")
            return result
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == max_attempts:
                raise

# Usage
def unreliable_api_call():
    # Simulate API call that might fail
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    return "Success"

try:
    result = retry_operation(unreliable_api_call)
except Exception:
    print("All attempts failed")
```

📁 [practical.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/exception-handling/practical.py)

---

## Best Practices

### ✅ Do

1. **Catch specific exceptions**

   ```python
   # ✅ GOOD
   try:
       result = int(value)
   except ValueError:
       print("Invalid number")
   ```

2. **Use finally for cleanup**

   ```python
   # ✅ GOOD
   try:
       file = open("file.txt")
   finally:
       file.close()
   ```

3. **Provide helpful error messages**

   ```python
   # ✅ GOOD
   raise ValueError(f"Age {age} is invalid. Must be 0-120")
   ```

4. **Log errors**
   ```python
   # ✅ GOOD
   except Exception as e:
       logger.error(f"Error occurred: {e}")
       raise
   ```

### ❌ Don't

1. **Don't catch all exceptions blindly**

   ```python
   # ❌ BAD
   try:
       # code
   except:
       pass  # Hides all errors!
   ```

2. **Don't use exceptions for control flow**

   ```python
   # ❌ BAD
   try:
       user = users[id]
   except KeyError:
       user = None

   # ✅ GOOD
   user = users.get(id)
   ```

3. **Don't ignore exceptions**
   ```python
   # ❌ BAD
   try:
       risky_operation()
   except Exception:
       pass  # Silent failure
   ```

---

## Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    ├── FileNotFoundError
    └── ... (many more)
```

---

## Quick Reference

### Basic Try-Except

```python
try:
    # risky code
except SpecificError:
    # handle error
```

### Multiple Exceptions

```python
try:
    # code
except (Error1, Error2) as e:
    # handle
```

### Try-Except-Else-Finally

```python
try:
    # code
except Error:
    # handle error
else:
    # runs if no error
finally:
    # always runs
```

### Raise Exception

```python
raise ValueError("Error message")
```

### Custom Exception

```python
class MyError(Exception):
    pass

raise MyError("Something went wrong")
```

---

## Summary

| Concept              | Purpose          | Example                          |
| -------------------- | ---------------- | -------------------------------- |
| **try-except**       | Handle errors    | `try: ... except: ...`           |
| **else**             | Runs if no error | `try: ... except: ... else: ...` |
| **finally**          | Always runs      | `try: ... finally: ...`          |
| **raise**            | Throw exception  | `raise ValueError()`             |
| **Custom exception** | Your own errors  | `class MyError(Exception):`      |
| **assert**           | Debug check      | `assert x > 0`                   |

**Remember:**

- **Catch specific exceptions**, not all
- **Use finally** for cleanup
- **Provide helpful messages**
- **Don't hide errors** with empty except
- **Custom exceptions** for domain-specific errors

📁 [basics.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/exception-handling/basics.py)  
📁 [common-exceptions.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/exception-handling/common-exceptions.py)  
📁 [raising-exceptions.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/exception-handling/raising-exceptions.py)  
📁 [practical.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/exception-handling/practical.py)
