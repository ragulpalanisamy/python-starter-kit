# Python Operators

## Table of Contents

1. [Arithmetic Operators](#arithmetic)
2. [Comparison Operators](#comparison)
3. [Logical Operators](#logical)
4. [Assignment Operators](#assignment)
5. [Bitwise Operators](#bitwise)
6. [Membership Operators](#membership)
7. [Identity Operators](#identity)
8. [Operator Precedence](#precedence)

---

## Arithmetic Operators {#arithmetic}

Used to perform mathematical operations.

| Operator | Name                | Example   | Result |
| -------- | ------------------- | --------- | ------ |
| `+`      | Addition            | `10 + 5`  | `15`   |
| `-`      | Subtraction         | `10 - 5`  | `5`    |
| `*`      | Multiplication      | `10 * 5`  | `50`   |
| `/`      | Division            | `10 / 5`  | `2.0`  |
| `//`     | Floor Division      | `10 // 3` | `3`    |
| `%`      | Modulus (Remainder) | `10 % 3`  | `1`    |
| `**`     | Exponentiation      | `2 ** 3`  | `8`    |

### Examples

```python
a = 20
b = 6

print(a + b)   # 26
print(a - b)   # 14
print(a * b)   # 120
print(a / b)   # 3.333...
print(a // b)  # 3 (floor division)
print(a % b)   # 2 (remainder)
print(a ** 2)  # 400 (20 squared)
```

### Practical Use Cases

- **Shopping cart total**: `quantity * price_per_item`
- **Check even/odd**: `number % 2 == 0`
- **Calculate area**: `pi * (radius ** 2)`
- **Split bill**: `total_bill / number_of_people`

📁 See: [arithmetic.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/operators/arithmetic.py)

---

## Comparison Operators {#comparison}

Used to compare two values. Returns `True` or `False`.

| Operator | Name                  | Example  | Result  |
| -------- | --------------------- | -------- | ------- |
| `==`     | Equal to              | `5 == 5` | `True`  |
| `!=`     | Not equal to          | `5 != 3` | `True`  |
| `>`      | Greater than          | `5 > 3`  | `True`  |
| `<`      | Less than             | `5 < 3`  | `False` |
| `>=`     | Greater than or equal | `5 >= 5` | `True`  |
| `<=`     | Less than or equal    | `5 <= 3` | `False` |

### Examples

```python
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= 10) # True
print(a <= 5)  # False
```

### Practical Use Cases

- **Age verification**: `age >= 18`
- **Password validation**: `len(password) >= 8`
- **Price comparison**: `sale_price < original_price`
- **Username check**: `username == "admin"`

📁 See: [comparison.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/operators/comparison.py)

---

## Logical Operators {#logical}

Used to combine conditional statements.

| Operator | Description                          | Example          | Result  |
| -------- | ------------------------------------ | ---------------- | ------- |
| `and`    | Returns True if both are True        | `True and False` | `False` |
| `or`     | Returns True if at least one is True | `True or False`  | `True`  |
| `not`    | Reverses the boolean value           | `not True`       | `False` |

### Truth Tables

**AND Operator:**
| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

**OR Operator:**
| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Examples

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
print(not b)    # True
```

### Practical Use Cases

- **Login validation**: `username == "admin" and password == "secret"`
- **Access control**: `age >= 18 and has_license`
- **Day off check**: `is_weekend or is_holiday`
- **Account status**: `is_active and not is_banned`

📁 See: [logical.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/operators/logical.py)

---

## Assignment Operators {#assignment}

Used to assign values to variables.

| Operator | Example   | Equivalent To |
| -------- | --------- | ------------- |
| `=`      | `x = 5`   | `x = 5`       |
| `+=`     | `x += 3`  | `x = x + 3`   |
| `-=`     | `x -= 3`  | `x = x - 3`   |
| `*=`     | `x *= 3`  | `x = x * 3`   |
| `/=`     | `x /= 3`  | `x = x / 3`   |
| `//=`    | `x //= 3` | `x = x // 3`  |
| `%=`     | `x %= 3`  | `x = x % 3`   |
| `**=`    | `x **= 3` | `x = x ** 3`  |

### Examples

```python
x = 10

x += 5   # x = 15
x -= 3   # x = 12
x *= 2   # x = 24
x /= 4   # x = 6.0
x //= 2  # x = 3.0
x %= 2   # x = 1.0
```

### Practical Use Cases

- **Shopping cart**: `cart_total += item_price`
- **Game score**: `score += 10`
- **Bank balance**: `balance -= withdrawal_amount`
- **Inventory**: `stock -= sold_quantity`

📁 See: [assignment.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/operators/assignment.py)

---

## Bitwise Operators {#bitwise}

Operate on binary representations of numbers.

| Operator | Name        | Example   | Result |
| -------- | ----------- | --------- | ------ |
| `&`      | AND         | `10 & 4`  | `0`    |
| `\|`     | OR          | `10 \| 4` | `14`   |
| `^`      | XOR         | `10 ^ 4`  | `14`   |
| `~`      | NOT         | `~10`     | `-11`  |
| `<<`     | Left Shift  | `10 << 2` | `40`   |
| `>>`     | Right Shift | `10 >> 2` | `2`    |

### Examples

```python
a = 10  # Binary: 1010
b = 4   # Binary: 0100

print(a & b)   # 0   (Binary: 0000)
print(a | b)   # 14  (Binary: 1110)
print(a ^ b)   # 14  (Binary: 1110)
print(~a)      # -11
print(a << 2)  # 40  (Multiply by 4)
print(a >> 2)  # 2   (Divide by 4)
```

### Practical Use Cases

- **Fast multiplication**: `num << 1` (multiply by 2)
- **Fast division**: `num >> 1` (divide by 2)
- **Check even/odd**: `num & 1` (returns 1 if odd, 0 if even)
- **Swap numbers**: Using XOR trick

📁 See: [bitwise.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/operators/bitwise.py)

---

## Membership Operators {#membership}

Test if a value exists in a sequence (list, tuple, string, etc.).

| Operator | Description                         | Example                       |
| -------- | ----------------------------------- | ----------------------------- |
| `in`     | Returns True if value exists        | `'a' in 'apple'` → `True`     |
| `not in` | Returns True if value doesn't exist | `'x' not in 'apple'` → `True` |

### Examples

```python
# List
fruits = ["apple", "banana", "mango"]
print("banana" in fruits)      # True
print("grape" not in fruits)   # True

# String
text = "Hello, World!"
print("World" in text)         # True
print("Python" not in text)    # True

# Tuple
numbers = (1, 2, 3, 4, 5)
print(3 in numbers)            # True

# Dictionary (checks keys)
user = {"name": "Ragul", "age": 25}
print("name" in user)          # True
print("email" not in user)     # True
```

### Practical Use Cases

- **Permission check**: `action in permissions`
- **Email validation**: `"@" in email and "." in email`
- **Banned words**: `word in banned_list`
- **File extension**: `".pdf" in filename`

📁 See: [membership.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/operators/membership.py)

---

## Identity Operators {#identity}

Compare the memory locations of two objects.

| Operator | Description                                     | Example      |
| -------- | ----------------------------------------------- | ------------ |
| `is`     | Returns True if both point to same object       | `a is b`     |
| `is not` | Returns True if both point to different objects | `a is not b` |

### Difference: `is` vs `==`

- `==` compares **values** (are they equal?)
- `is` compares **identity** (are they the same object in memory?)

### Examples

```python
# Integers (small integers are cached)
a = 10
b = 10
print(a is b)  # True (same object)

# Lists (different objects even with same values)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)  # True (same values)
print(list1 is list2)  # False (different objects)
print(list1 is list3)  # True (same object)

# None comparison (always use 'is')
value = None
print(value is None)      # True ✅
print(value == None)      # True (but 'is' is preferred)
```

### Practical Use Cases

- **None check**: `value is None` (preferred over `value == None`)
- **Object comparison**: Check if two variables reference the same object
- **Singleton check**: `is True`, `is False`

📁 See: [identity.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/operators/identity.py)

---

## Operator Precedence {#precedence}

When multiple operators are used in an expression, Python follows this order (highest to lowest):

| Priority | Operator                                                         | Description              |
| -------- | ---------------------------------------------------------------- | ------------------------ |
| 1        | `()`                                                             | Parentheses              |
| 2        | `**`                                                             | Exponentiation           |
| 3        | `~`, `+`, `-`                                                    | Unary operators          |
| 4        | `*`, `/`, `//`, `%`                                              | Multiplication, Division |
| 5        | `+`, `-`                                                         | Addition, Subtraction    |
| 6        | `<<`, `>>`                                                       | Bitwise shifts           |
| 7        | `&`                                                              | Bitwise AND              |
| 8        | `^`                                                              | Bitwise XOR              |
| 9        | `\|`                                                             | Bitwise OR               |
| 10       | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | Comparison               |
| 11       | `not`                                                            | Logical NOT              |
| 12       | `and`                                                            | Logical AND              |
| 13       | `or`                                                             | Logical OR               |

### Examples

```python
# Without parentheses
result = 10 + 5 * 2
print(result)  # 20 (multiplication first)

# With parentheses
result = (10 + 5) * 2
print(result)  # 30 (addition first)

# Complex expression
result = 2 + 3 * 4 ** 2
print(result)  # 50 (4**2=16, 3*16=48, 2+48=50)

# Logical operators
result = True or False and False
print(result)  # True ('and' before 'or')

result = (True or False) and False
print(result)  # False (parentheses first)
```

### Best Practice

**Use parentheses** to make your code more readable, even when not strictly necessary:

```python
# Less clear
if age >= 18 and has_license or is_instructor:
    pass

# More clear
if (age >= 18 and has_license) or is_instructor:
    pass
```

---

## Summary

| Category       | Operators                           | Purpose            |
| -------------- | ----------------------------------- | ------------------ |
| **Arithmetic** | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Math operations    |
| **Comparison** | `==`, `!=`, `>`, `<`, `>=`, `<=`    | Compare values     |
| **Logical**    | `and`, `or`, `not`                  | Combine conditions |
| **Assignment** | `=`, `+=`, `-=`, `*=`, etc.         | Assign values      |
| **Bitwise**    | `&`, `\|`, `^`, `~`, `<<`, `>>`     | Binary operations  |
| **Membership** | `in`, `not in`                      | Check membership   |
| **Identity**   | `is`, `is not`                      | Compare objects    |

**Key Takeaways:**

- Use `==` to compare values, `is` to compare object identity
- Always use `is` when comparing with `None`
- Logical operators: `and` requires both, `or` requires at least one
- Assignment operators (`+=`, `-=`) are shortcuts for common operations
- Use parentheses to make operator precedence clear
