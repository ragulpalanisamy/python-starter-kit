# Python Strings - Quick Reference

## Table of Contents

1. [String Basics](#basics)
2. [String Methods](#methods)
3. [String Formatting](#formatting)
4. [Practical Examples](#practical)

---

## String Basics {#basics}

### Creating Strings

```python
single = 'Hello'
double = "World"
triple = '''Multi
line'''
```

### String Operations

| Operation     | Example                   | Result          |
| ------------- | ------------------------- | --------------- |
| Concatenation | `"Hello" + " " + "World"` | `"Hello World"` |
| Repetition    | `"Ha" * 3`                | `"HaHaHa"`      |
| Length        | `len("Python")`           | `6`             |
| Membership    | `"a" in "apple"`          | `True`          |

### Indexing & Slicing

```python
text = "Python"

# Indexing (0-based)
text[0]    # 'P' (first)
text[-1]   # 'n' (last)

# Slicing [start:end:step]
text[0:3]  # 'Pyt'
text[2:]   # 'thon'
text[:4]   # 'Pyth'
text[::2]  # 'Pto' (every 2nd)
text[::-1] # 'nohtyP' (reverse)
```

📁 [basics.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/strings/basics.py)

---

## String Methods {#methods}

### Case Conversion

| Method         | Example                 | Result          |
| -------------- | ----------------------- | --------------- |
| `upper()`      | `"hello".upper()`       | `"HELLO"`       |
| `lower()`      | `"HELLO".lower()`       | `"hello"`       |
| `title()`      | `"hello world".title()` | `"Hello World"` |
| `capitalize()` | `"hello".capitalize()`  | `"Hello"`       |
| `swapcase()`   | `"Hello".swapcase()`    | `"hELLO"`       |

### Whitespace

| Method     | Example             | Result   |
| ---------- | ------------------- | -------- |
| `strip()`  | `"  hi  ".strip()`  | `"hi"`   |
| `lstrip()` | `"  hi  ".lstrip()` | `"hi  "` |
| `rstrip()` | `"  hi  ".rstrip()` | `"  hi"` |

### Search & Replace

| Method              | Description                                | Example                                 |
| ------------------- | ------------------------------------------ | --------------------------------------- |
| `find(sub)`         | Find substring (returns -1 if not found)   | `"hello".find("ll")` → `2`              |
| `index(sub)`        | Find substring (raises error if not found) | `"hello".index("ll")` → `2`             |
| `count(sub)`        | Count occurrences                          | `"hello".count("l")` → `2`              |
| `startswith(sub)`   | Check if starts with                       | `"hello".startswith("he")` → `True`     |
| `endswith(sub)`     | Check if ends with                         | `"hello".endswith("lo")` → `True`       |
| `replace(old, new)` | Replace substring                          | `"hi".replace("i", "ello")` → `"hello"` |

### Split & Join

```python
# Split
"a,b,c".split(',')        # ['a', 'b', 'c']
"hello world".split()     # ['hello', 'world']

# Join
"-".join(['a', 'b', 'c']) # 'a-b-c'
" ".join(['hi', 'there']) # 'hi there'
```

### Validation

| Method      | Checks if...   | Example                            |
| ----------- | -------------- | ---------------------------------- |
| `isalpha()` | All alphabetic | `"abc".isalpha()` → `True`         |
| `isdigit()` | All digits     | `"123".isdigit()` → `True`         |
| `isalnum()` | Alphanumeric   | `"abc123".isalnum()` → `True`      |
| `isspace()` | All whitespace | `"   ".isspace()` → `True`         |
| `isupper()` | All uppercase  | `"ABC".isupper()` → `True`         |
| `islower()` | All lowercase  | `"abc".islower()` → `True`         |
| `istitle()` | Title case     | `"Hello World".istitle()` → `True` |

📁 [methods.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/strings/methods.py)

---

## String Formatting {#formatting}

### 1. F-Strings (Recommended) ⭐

```python
name = "Ragul"
age = 25
price = 99.99

# Basic
f"Hello, {name}!"                    # "Hello, Ragul!"
f"{name} is {age} years old"         # "Ragul is 25 years old"

# Expressions
f"10 + 5 = {10 + 5}"                 # "10 + 5 = 15"

# Formatting
f"Price: ₹{price:.2f}"               # "Price: ₹99.99"
f"{1234567:,}"                       # "1,234,567"
f"{0.85:.1%}"                        # "85.0%"

# Alignment
f"{'left':<10}"                      # "left      "
f"{'right':>10}"                     # "     right"
f"{'center':^10}"                    # "  center  "

# Padding
f"{42:05d}"                          # "00042"
```

### 2. format() Method

```python
"Hello, {}!".format(name)                      # Positional
"{1} is {0}".format(age, name)                 # By position
"{n} is {a}".format(n=name, a=age)            # Named
"Price: ₹{:.2f}".format(price)                # Formatting
```

### 3. % Formatting (Old Style)

```python
"Hello, %s!" % name                  # String
"%s is %d years old" % (name, age)   # Multiple
"Price: ₹%.2f" % price               # Float
```

### Format Specifiers

| Specifier | Meaning               | Example                          |
| --------- | --------------------- | -------------------------------- |
| `:d`      | Integer               | `f"{42:d}"` → `"42"`             |
| `:f`      | Float                 | `f"{3.14:f}"` → `"3.140000"`     |
| `:.2f`    | 2 decimal places      | `f"{3.14159:.2f}"` → `"3.14"`    |
| `:,`      | Comma separator       | `f"{1000:,}"` → `"1,000"`        |
| `:%`      | Percentage            | `f"{0.5:%}"` → `"50.000000%"`    |
| `:<10`    | Left align (width 10) | `f"{'hi':<10}"` → `"hi        "` |
| `:>10`    | Right align           | `f"{'hi':>10}"` → `"        hi"` |
| `:^10`    | Center align          | `f"{'hi':^10}"` → `"    hi    "` |
| `:05d`    | Zero padding          | `f"{42:05d}"` → `"00042"`        |

📁 [formatting.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/strings/formatting.py)

---

## Practical Examples {#practical}

### 1. Email Validation

```python
email = "user@example.com"
if "@" in email and "." in email.split("@")[1]:
    print("✅ Valid")
```

### 2. Password Strength

```python
password = "Secret@123"
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
is_strong = all([has_upper, has_lower, has_digit, len(password) >= 8])
```

### 3. Name Formatting

```python
name = "  ragul PALANISAMY  "
formatted = name.strip().title()  # "Ragul Palanisamy"
```

### 4. URL Slug

```python
title = "Python String Tutorial"
slug = title.lower().replace(" ", "-")  # "python-string-tutorial"
```

### 5. Extract Domain

```python
email = "user@company.com"
domain = email.split("@")[1]  # "company.com"
```

### 6. Reverse Words

```python
sentence = "Hello World"
reversed = " ".join(sentence.split()[::-1])  # "World Hello"
```

### 7. Count Vowels

```python
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for c in text if c in vowels)  # 3
```

### 8. Palindrome Check

```python
word = "radar"
is_palindrome = word == word[::-1]  # True
```

### 9. Mask Credit Card

```python
card = "1234567890123456"
masked = "*" * 12 + card[-4:]  # "************3456"
```

### 10. Remove Duplicates

```python
text = "programming"
unique = "".join(dict.fromkeys(text))  # "progamin"
```

📁 [practical.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/strings/practical.py)

---

## Quick Tips

### ✅ Best Practices

1. **Use f-strings** for formatting (Python 3.6+)
2. **Use `.strip()`** to remove whitespace
3. **Strings are immutable** - methods return new strings
4. **Use `in`** for membership testing
5. **Use `.join()`** for concatenating many strings

### ⚠️ Common Mistakes

```python
# ❌ BAD - Modifying strings in loop
result = ""
for word in words:
    result += word  # Creates new string each time

# ✅ GOOD - Use join
result = "".join(words)

# ❌ BAD - Using + for many strings
text = str1 + str2 + str3 + str4

# ✅ GOOD - Use f-string or join
text = f"{str1}{str2}{str3}{str4}"
```

---

## Summary

| Category   | Key Methods                     | Use Case                      |
| ---------- | ------------------------------- | ----------------------------- |
| **Case**   | `upper()`, `lower()`, `title()` | Formatting names, comparison  |
| **Clean**  | `strip()`, `replace()`          | Remove whitespace, clean data |
| **Search** | `find()`, `count()`, `in`       | Find substrings               |
| **Split**  | `split()`, `join()`             | Parse CSV, build sentences    |
| **Check**  | `isdigit()`, `isalpha()`        | Validate input                |
| **Format** | f-strings, `format()`           | Display data                  |

**Remember:**

- Strings are **immutable** (cannot be changed)
- Indexing starts at **0**
- Negative indices count from the **end**
- Use **f-strings** for modern formatting
- Always **validate** user input
