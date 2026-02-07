# Python User Input

## Table of Contents

1. [Basic Input - input()](#basic-input)
2. [Type Casting](#type-casting)
3. [Multiple Inputs](#multiple-inputs)
4. [Error Handling](#error-handling)
5. [Input Validation](#validation)
6. [Command-Line Arguments](#command-line)
7. [Other Input Methods](#other-methods)
8. [Best Practices](#best-practices)

---

## Basic Input - `input()` {#basic-input}

The `input()` function reads a line from the user and **always returns a string**.

### Syntax

```python
input([prompt])
```

- **`prompt`** (optional): A string displayed to the user before reading input

### Examples

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Check the type
print(type(name))  # <class 'str'>
```

### Key Points

- Always returns a **string**, even if the user enters numbers
- Waits for the user to press Enter
- The prompt parameter is optional but recommended for clarity

---

## Type Casting {#type-casting}

Convert string input to other data types using type casting functions.

### Common Conversions

| Function  | Converts to | Example                    |
| --------- | ----------- | -------------------------- |
| `int()`   | Integer     | `int(input())`             |
| `float()` | Float       | `float(input())`           |
| `str()`   | String      | `str(input())` (redundant) |
| `bool()`  | Boolean     | `bool(input())`            |

### Examples

```python
# String to integer
age = int(input("Enter your age: "))
print(f"You are {age} years old")

# String to float
height = float(input("Enter your height in meters: "))
print(f"Your height is {height}m")

# String to boolean (empty string is False, non-empty is True)
response = bool(input("Enter something: "))
print(f"Boolean value: {response}")
```

### ⚠️ Warning

Type casting can raise `ValueError` if the input cannot be converted:

```python
age = int(input("Enter age: "))
# If user enters "hello" → ValueError: invalid literal for int()
```

---

## Multiple Inputs {#multiple-inputs}

Use `split()` to read multiple values from a single input line.

### Using `split()`

```python
# Split by space (default)
first_name, last_name = input("Enter first and last name: ").split()
print(f"First: {first_name}, Last: {last_name}")

# Split by custom separator
a, b, c = input("Enter three numbers (comma-separated): ").split(',')
print(f"Numbers: {a}, {b}, {c}")

# Split and convert to integers
nums = list(map(int, input("Enter numbers: ").split()))
print(f"Numbers: {nums}")
print(f"Sum: {sum(nums)}")
```

### Reading a List of Values

```python
# Read multiple integers
numbers = list(map(int, input("Enter numbers: ").split()))

# Read multiple floats
prices = list(map(float, input("Enter prices: ").split()))

# Read multiple strings
words = input("Enter words: ").split()
```

---

## Error Handling {#error-handling}

Always handle potential errors when converting user input.

### Using `try-except`

```python
# Basic error handling
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Invalid input! Please enter a valid number.")
```

### Input Validation with Retry

```python
# Keep asking until valid input
while True:
    try:
        age = int(input("Enter your age: "))
        if 0 < age < 120:
            print(f"Valid age: {age}")
            break
        else:
            print("Age must be between 1 and 119!")
    except ValueError:
        print("Invalid input! Please enter a number.")
```

### Safe Input Function

```python
def safe_int_input(prompt, default=0):
    """Safely get integer input with a default value"""
    try:
        return int(input(prompt))
    except ValueError:
        print(f"Invalid input. Using default: {default}")
        return default

age = safe_int_input("Enter age: ", default=18)
```

---

## Input Validation {#validation}

Validate user input to ensure data quality.

### Common Validation Techniques

#### 1. Non-Empty Input

```python
username = input("Enter username: ").strip()
if username:
    print(f"Username: {username}")
else:
    print("Username cannot be empty!")
```

#### 2. Email Validation

```python
email = input("Enter email: ")
if "@" in email and "." in email:
    print("Valid email format")
else:
    print("Invalid email format")
```

#### 3. Range Validation

```python
age = int(input("Enter age: "))
if 0 < age < 120:
    print("Valid age")
else:
    print("Age out of range!")
```

#### 4. Choice Validation

```python
choice = input("Choose (yes/no): ").lower()
if choice in ["yes", "no"]:
    print(f"You chose: {choice}")
else:
    print("Invalid choice!")
```

#### 5. Length Validation

```python
password = input("Enter password: ")
if len(password) >= 8:
    print("Password accepted")
else:
    print("Password must be at least 8 characters!")
```

---

## Command-Line Arguments {#command-line}

Use `sys.argv` to read arguments passed when running the script.

### Using `sys.argv`

```python
import sys

# sys.argv[0] → script name
# sys.argv[1] → first argument
# sys.argv[2] → second argument
# ...

print(f"Script name: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")

# Check if arguments were provided
if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
    print("No arguments provided")
    print("Usage: python3 script.py <name>")
```

### Running with Arguments

```bash
# Command line
python3 index.py Ragul

# Output
# Script name: index.py
# Arguments: ['Ragul']
# Hello, Ragul!
```

### Practical Example

```python
import sys

if len(sys.argv) > 1:
    full_name = sys.argv[1]
    email = full_name.lower().replace(" ", "") + "@company.com"
    print(f"Name: {full_name}")
    print(f"Email: {email}")
else:
    print("Usage: python3 script.py 'Your Name'")
```

---

## Other Input Methods {#other-methods}

### 1. `sys.stdin.readline()`

Reads a line from standard input (includes newline character).

```python
import sys

print("Enter your name: ", end="")
name = sys.stdin.readline().strip()  # strip() removes newline
print(f"Hello, {name}!")
```

### 2. `getpass` - Hidden Input

For password input (characters are not displayed).

```python
from getpass import getpass

password = getpass("Enter password: ")
print(f"Password length: {len(password)}")
```

### 3. File Input

Read input from a file instead of the keyboard.

```python
with open("input.txt", "r") as f:
    name = f.readline().strip()
    age = int(f.readline().strip())
    print(f"Name: {name}, Age: {age}")
```

### 4. `argparse` - Advanced Command-Line Arguments

For complex command-line interfaces.

```python
import argparse

parser = argparse.ArgumentParser(description="Process user data")
parser.add_argument("name", help="User's name")
parser.add_argument("--age", type=int, help="User's age")

args = parser.parse_args()
print(f"Name: {args.name}")
if args.age:
    print(f"Age: {args.age}")
```

---

## Best Practices {#best-practices}

### 1. Always Provide Clear Prompts

```python
# ✅ GOOD - Clear prompt
name = input("Enter your full name: ")

# ❌ BAD - No prompt
name = input()
```

### 2. Use Type Casting Carefully

```python
# ✅ GOOD - With error handling
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid input!")

# ❌ BAD - No error handling
age = int(input("Enter age: "))  # Can crash
```

### 3. Validate User Input

```python
# ✅ GOOD - Validate before using
username = input("Enter username: ").strip()
if username and len(username) >= 3:
    print(f"Welcome, {username}!")
else:
    print("Username must be at least 3 characters!")

# ❌ BAD - No validation
username = input("Enter username: ")
```

### 4. Use `.strip()` to Remove Whitespace

```python
# ✅ GOOD - Remove leading/trailing spaces
name = input("Enter name: ").strip()

# ❌ BAD - Keeps extra spaces
name = input("Enter name: ")
```

### 5. Provide Default Values

```python
# ✅ GOOD - Default value
name = input("Enter name (default: Guest): ") or "Guest"
print(f"Hello, {name}!")
```

### 6. Use Descriptive Variable Names

```python
# ✅ GOOD - Clear variable names
user_email = input("Enter email: ")
user_age = int(input("Enter age: "))

# ❌ BAD - Unclear names
x = input("Enter email: ")
y = int(input("Enter age: "))
```

---

## Practical Examples

### Example 1: Simple Calculator

```python
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operation"

    print(f"Result: {result}")
except ValueError:
    print("Invalid number input!")
```

### Example 2: User Registration

```python
print("=== User Registration ===")

username = input("Username: ").strip()
email = input("Email: ").strip()
age = input("Age: ").strip()

# Validate
if not username:
    print("Error: Username required")
elif "@" not in email:
    print("Error: Invalid email")
elif not age.isdigit():
    print("Error: Age must be a number")
else:
    print("\n✅ Registration successful!")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")
```

---

## Summary

| Method         | Use Case          | Example                       |
| -------------- | ----------------- | ----------------------------- |
| `input()`      | Basic text input  | `name = input("Name: ")`      |
| `int(input())` | Integer input     | `age = int(input("Age: "))`   |
| `split()`      | Multiple values   | `a, b = input().split()`      |
| `sys.argv`     | Command-line args | `name = sys.argv[1]`          |
| `getpass()`    | Password input    | `pwd = getpass("Password: ")` |

**Key Takeaways:**

- `input()` always returns a string
- Use type casting (`int()`, `float()`) to convert input
- Always handle errors with `try-except`
- Validate input before using it
- Use `.strip()` to remove whitespace
- Provide clear prompts to users

📁 See: [index.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/input/index.py) for complete examples
