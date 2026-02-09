# Python Control Flow - Conditionals & Loops

## Table of Contents

1. [Conditional Statements](#conditionals)
2. [For Loops](#for-loops)
3. [While Loops](#while-loops)
4. [Loop Control](#loop-control)
5. [Practical Examples](#practical)

---

## Conditional Statements {#conditionals}

Control the flow of your program based on conditions.

### if Statement

```python
age = 20
if age >= 18:
    print("You are an adult")
```

### if-else Statement

```python
temperature = 25
if temperature > 30:
    print("It's hot!")
else:
    print("It's pleasant!")
```

### if-elif-else Statement

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### Nested if

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive!")
    else:
        print("You need a license")
```

### Multiple Conditions

| Operator | Description               | Example                     |
| -------- | ------------------------- | --------------------------- |
| `and`    | Both must be True         | `age >= 18 and has_license` |
| `or`     | At least one must be True | `is_weekend or is_holiday`  |
| `not`    | Reverses the condition    | `not is_banned`             |

```python
# AND
if username == "admin" and password == "secret":
    print("Login successful")

# OR
if is_weekend or is_holiday:
    print("Day off!")

# NOT
if not is_banned:
    print("Account active")
```

### Ternary Operator (One-line if-else)

```python
# Syntax: value_if_true if condition else value_if_false
status = "Adult" if age >= 18 else "Minor"

# Practical
discount = 0.2 if price > 500 else 0.1
```

📁 [conditionals.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/control-flow/conditionals.py)

---

## For Loops {#for-loops}

Iterate over sequences (lists, strings, ranges, etc.).

### Loop Through List

```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
```

### Loop Through String

```python
for char in "Python":
    print(char)  # P y t h o n
```

### Loop with range()

| Syntax                     | Example           | Output          |
| -------------------------- | ----------------- | --------------- |
| `range(stop)`              | `range(5)`        | `0, 1, 2, 3, 4` |
| `range(start, stop)`       | `range(2, 6)`     | `2, 3, 4, 5`    |
| `range(start, stop, step)` | `range(0, 10, 2)` | `0, 2, 4, 6, 8` |

```python
# 0 to 4
for i in range(5):
    print(i)

# 2 to 5
for i in range(2, 6):
    print(i)

# Even numbers 0 to 8
for i in range(0, 10, 2):
    print(i)
```

### enumerate() - Get Index + Value

```python
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")
# Output:
# 0: red
# 1: green
# 2: blue
```

### Loop Through Dictionary

```python
user = {"name": "Ragul", "age": 25}

# Keys only
for key in user:
    print(key)

# Values only
for value in user.values():
    print(value)

# Key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")
```

### Nested Loops

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()
# Output:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)
```

### List Comprehension (Compact For Loop)

```python
# Normal loop
squares = []
for i in range(5):
    squares.append(i ** 2)

# List comprehension (one line)
squares = [i ** 2 for i in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [i for i in range(10) if i % 2 == 0]  # [0, 2, 4, 6, 8]
```

📁 [for-loops.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/control-flow/for-loops.py)

---

## While Loops {#while-loops}

Repeat code while a condition is True.

### Basic While Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### While with Condition

```python
password = ""
attempts = 0

while password != "secret" and attempts < 3:
    password = input("Enter password: ")
    attempts += 1
```

### Infinite Loop with break

```python
counter = 0
while True:
    print(counter)
    counter += 1
    if counter >= 5:
        break  # Exit loop
```

### While with continue

```python
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue  # Skip 3
    print(num)  # Prints: 1, 2, 4, 5
```

### While-else

The `else` block runs when the loop completes normally (no `break`).

```python
n = 0
while n < 3:
    print(n)
    n += 1
else:
    print("Loop completed!")
```

📁 [while-loops.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/control-flow/while-loops.py)

---

## Loop Control {#loop-control}

Control loop execution with `break`, `continue`, and `pass`.

### break - Exit Loop

```python
for i in range(10):
    if i == 5:
        break  # Exit loop
    print(i)  # Prints: 0, 1, 2, 3, 4
```

### continue - Skip Iteration

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Prints: 1, 3, 5, 7, 9
```

### pass - Do Nothing

Placeholder for future code.

```python
for i in range(5):
    if i == 2:
        pass  # TODO: Add logic later
    print(i)
```

### Comparison

| Statement  | Action                 | Use Case                      |
| ---------- | ---------------------- | ----------------------------- |
| `break`    | Exit loop completely   | Found what you're looking for |
| `continue` | Skip to next iteration | Skip certain values           |
| `pass`     | Do nothing             | Placeholder for future code   |

📁 [loop-control.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/control-flow/loop-control.py)

---

## Practical Examples {#practical}

### 1. Menu System

```python
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        # Add logic
    elif choice == "2":
        # Subtract logic
    elif choice == "3":
        break
```

### 2. FizzBuzz

```python
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### 3. Prime Number Checker

```python
num = 17
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

print(f"{num} is {'prime' if is_prime else 'not prime'}")
```

### 4. Multiplication Table

```python
n = 5
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")
```

### 5. Pattern Printing

```python
rows = 5
for i in range(1, rows + 1):
    print("* " * i)
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
```

### 6. Sum of Numbers

```python
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")  # 150
```

### 7. Find Maximum

```python
numbers = [45, 23, 89, 12, 67]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Max: {max_num}")  # 89
```

### 8. Count Vowels

```python
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"Vowels: {count}")  # 3
```

### 9. Reverse String

```python
text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)  # "nohtyP"
```

### 10. Shopping Cart

```python
cart = {"apple": 50, "banana": 30, "mango": 80}
total = 0

for item, price in cart.items():
    print(f"{item}: ₹{price}")
    total += price

if total > 100:
    discount = total * 0.1
    total -= discount
    print(f"Discount applied! Final: ₹{total}")
```

📁 [practical.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/control-flow/practical.py)

---

## Quick Reference

### Conditionals

```python
# if-elif-else
if condition1:
    # code
elif condition2:
    # code
else:
    # code

# Ternary
result = value_if_true if condition else value_if_false
```

### For Loops

```python
# List
for item in list:
    # code

# Range
for i in range(start, stop, step):
    # code

# Enumerate
for index, value in enumerate(list):
    # code

# Dictionary
for key, value in dict.items():
    # code
```

### While Loops

```python
# Basic
while condition:
    # code

# Infinite with break
while True:
    # code
    if condition:
        break
```

### Loop Control

```python
break      # Exit loop
continue   # Skip to next iteration
pass       # Do nothing (placeholder)
```

---

## Best Practices

### ✅ Do

- Use `for` when you know the number of iterations
- Use `while` when the number of iterations is unknown
- Use `break` to exit early when you find what you need
- Use `continue` to skip invalid data
- Use list comprehensions for simple transformations

### ❌ Don't

```python
# ❌ BAD - Infinite loop without break
while True:
    print("Forever!")

# ✅ GOOD - Infinite loop with exit condition
while True:
    if should_exit:
        break

# ❌ BAD - Modifying list while iterating
for item in items:
    items.remove(item)  # Can cause issues

# ✅ GOOD - Create new list or use copy
for item in items[:]:
    items.remove(item)
```

---

## Summary

| Concept          | Purpose                        | Example                  |
| ---------------- | ------------------------------ | ------------------------ |
| **if-elif-else** | Make decisions                 | `if age >= 18: ...`      |
| **for loop**     | Iterate over sequence          | `for i in range(5): ...` |
| **while loop**   | Repeat while condition is True | `while count < 10: ...`  |
| **break**        | Exit loop                      | `if found: break`        |
| **continue**     | Skip iteration                 | `if invalid: continue`   |
| **pass**         | Placeholder                    | `if x: pass`             |

**Remember:**

- Indentation matters in Python!
- Use `for` for known iterations, `while` for unknown
- `break` exits the loop, `continue` skips to next iteration
- Ternary operator for simple if-else: `x if condition else y`
