# 📏 PEP 8 - Python Style Guide

> **Write clean, readable Python code that everyone can understand**

PEP 8 is Python's official style guide. It tells you how to format your code so it looks professional and is easy to read.

---

## 🎯 Why PEP 8?

```python
# Bad - Hard to read
def f(x,y):return x+y

# Good - Easy to read
def add(x, y):
    return x + y
```

**Benefits:**

- ✅ Code is easier to read
- ✅ Teams work better together
- ✅ Looks professional
- ✅ Fewer bugs

---

## 📐 Key Rules (Simple Version)

### 1️⃣ **Indentation** - Use 4 Spaces

```python
# ✅ Good
def greet(name):
    if name:
        print(f"Hello, {name}")
    else:
        print("Hello, World")

# ❌ Bad - 2 spaces or tabs
def greet(name):
  if name:
      print(f"Hello, {name}")
```

---

### 2️⃣ **Line Length** - Max 79 Characters

```python
# ✅ Good - Short lines
message = "This is a short message"

# ❌ Bad - Too long
message = "This is a very long message that goes on and on and exceeds the recommended 79 character limit"

# ✅ Good - Split long lines
message = (
    "This is a very long message that goes on and on "
    "but we split it into multiple lines"
)
```

---

### 3️⃣ **Blank Lines** - Separate Functions

```python
# ✅ Good
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# ❌ Bad - No spacing
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
```

**Rules:**

- 2 blank lines before functions
- 1 blank line inside functions (if needed)

---

### 4️⃣ **Spaces** - Around Operators

```python
# ✅ Good
x = 5
y = x + 10
result = x * y

# ❌ Bad
x=5
y=x+10
result=x*y
```

**Rules:**

- Space around `=`, `+`, `-`, `*`, `/`
- Space after commas: `func(a, b, c)`
- No space inside brackets: `list[0]` not `list[ 0 ]`

---

### 5️⃣ **Naming Conventions**

```python
# ✅ Good
user_name = "Ragul"           # Variables: lowercase_with_underscores
MAX_SIZE = 100               # Constants: UPPERCASE_WITH_UNDERSCORES

def calculate_total():       # Functions: lowercase_with_underscores
    pass

class UserProfile:           # Classes: CapitalizedWords
    pass

# ❌ Bad
UserName = "Ragul"            # Don't capitalize variables
def CalculateTotal():        # Don't capitalize functions
class user_profile:          # Don't lowercase classes
```

**Quick Reference:**
| Type | Style | Example |
|------|-------|---------|
| Variables | `snake_case` | `user_name` |
| Functions | `snake_case` | `get_user()` |
| Classes | `PascalCase` | `UserProfile` |
| Constants | `UPPER_CASE` | `MAX_SIZE` |

---

### 6️⃣ **Imports** - At the Top

```python
# ✅ Good - Organized imports
import os
import sys

from math import sqrt, pow
from datetime import datetime

# Your code here
def main():
    pass


# ❌ Bad - Imports scattered
def main():
    import os  # Don't import inside functions
    pass
```

**Order:**

1. Standard library (`os`, `sys`)
2. Third-party packages (`requests`, `numpy`)
3. Your own modules

---

### 7️⃣ **Comments** - Explain Why, Not What

```python
# ✅ Good - Explains WHY
# Use binary search because list is sorted and large
result = binary_search(data, target)

# ❌ Bad - States the obvious
# This adds 1 to x
x = x + 1
```

---

### 8️⃣ **Docstrings** - Document Functions

```python
# ✅ Good
def add(a, b):
    """Add two numbers and return the result.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b


# ❌ Bad - No documentation
def add(a, b):
    return a + b
```

---

## 🎨 Before & After Examples

### Example 1: Function Definition

```python
# ❌ Bad
def calculate(x,y,z):
  result=x+y*z
  return result

# ✅ Good
def calculate(x, y, z):
    """Calculate x + (y * z)."""
    result = x + y * z
    return result
```

### Example 2: Conditionals

```python
# ❌ Bad
if x>5:print("Big")
else:print("Small")

# ✅ Good
if x > 5:
    print("Big")
else:
    print("Small")
```

### Example 3: Lists

```python
# ❌ Bad
numbers=[1,2,3,4,5]
result=sum(numbers)

# ✅ Good
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
```

---

## 🔧 Quick Checklist

Before you commit code, check:

- [ ] 4 spaces for indentation (not tabs)
- [ ] Lines under 79 characters
- [ ] 2 blank lines between functions
- [ ] Spaces around operators (`x = 5`, not `x=5`)
- [ ] `snake_case` for variables and functions
- [ ] `PascalCase` for classes
- [ ] Imports at the top
- [ ] Docstrings for functions
- [ ] Meaningful variable names

---

## 🛠️ Tools to Help

### Automatic Formatting

```bash
# Install black (auto-formatter)
pip install black

# Format your code
black your_file.py
```

### Check Style

```bash
# Install flake8 (style checker)
pip install flake8

# Check your code
flake8 your_file.py
```

---

## 💡 Pro Tips

1. **Use an IDE** - VS Code, PyCharm show PEP 8 warnings
2. **Install black** - Auto-formats your code
3. **Read error messages** - They tell you what's wrong
4. **Practice** - It becomes natural over time
5. **Don't stress** - Focus on readability first

---

## 📚 Common Mistakes (Beginners)

### ❌ Mistake 1: No spaces

```python
x=5+3  # Bad
x = 5 + 3  # Good
```

### ❌ Mistake 2: Wrong indentation

```python
def hello():
  print("Hi")  # Bad (2 spaces)

def hello():
    print("Hi")  # Good (4 spaces)
```

### ❌ Mistake 3: Long lines

```python
# Bad - One long line
result = some_function(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

# Good - Split it
result = some_function(
    arg1, arg2, arg3, arg4,
    arg5, arg6, arg7, arg8
)
```

---

## 🎓 Summary

**Remember these 3 things:**

1. **4 spaces** for indentation
2. **Spaces around operators** (`x = 5`)
3. **snake_case** for variables and functions

**Everything else you'll learn with practice!**

---

## 📖 Want to Learn More?

- Official PEP 8: https://peps.python.org/pep-0008/
- Use `black` to auto-format
- Use `flake8` to check style

---

_Write clean code, make Python proud! 🐍_
