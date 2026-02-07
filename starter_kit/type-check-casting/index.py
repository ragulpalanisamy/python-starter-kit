# ============================================
# Type Checking, Type Casting & Type Hinting
# ============================================

# ============================================
# 1. TYPE CHECKING
# ============================================

print("=" * 50)
print("TYPE CHECKING")
print("=" * 50)

# Using type() function to check data types
user_id = '123'
age = 25
price = 99.99
is_active = True
items = [1, 2, 3]

print(f"user_id: {user_id} -> {type(user_id)}")
print(f"age: {age} -> {type(age)}")
print(f"price: {price} -> {type(price)}")
print(f"is_active: {is_active} -> {type(is_active)}")
print(f"items: {items} -> {type(items)}")

# Using isinstance() for type checking (preferred method)
print(f"\nIs user_id a string? {isinstance(user_id, str)}")
print(f"Is age an integer? {isinstance(age, int)}")
print(f"Is price a float? {isinstance(price, float)}")
print(f"Is items a list? {isinstance(items, list)}")

print()

# ============================================
# 2. TYPE CASTING - SUCCESSFUL CONVERSIONS
# ============================================

print("=" * 50)
print("TYPE CASTING - SUCCESSFUL CONVERSIONS")
print("=" * 50)

# String number to integer
x = '10'
x_int = int(x)
print(f"String to int: '{x}' -> {x_int} (type: {type(x_int)})")

# String float to float
y = '10.5'
y_float = float(y)
print(f"String to float: '{y}' -> {y_float} (type: {type(y_float)})")

# Integer to float
num = 42
num_float = float(num)
print(f"Int to float: {num} -> {num_float} (type: {type(num_float)})")

# Float to integer (truncates decimal)
pi = 3.14159
pi_int = int(pi)
print(f"Float to int: {pi} -> {pi_int} (type: {type(pi_int)}) [truncated]")

# Integer to string
count = 100
count_str = str(count)
print(f"Int to string: {count} -> '{count_str}' (type: {type(count_str)})")

# Boolean to integer
is_true = True
is_false = False
print(f"Bool to int: True -> {int(is_true)}, False -> {int(is_false)}")

# Integer to boolean (0 is False, non-zero is True)
print(f"Int to bool: 0 -> {bool(0)}, 1 -> {bool(1)}, 42 -> {bool(42)}")

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"List to tuple: {my_list} -> {my_tuple} (type: {type(my_tuple)})")

# String to list
text = "hello"
text_list = list(text)
print(f"String to list: '{text}' -> {text_list}")

print()

# ============================================
# 3. TYPE CASTING - LIMITATIONS & ERRORS
# ============================================

print("=" * 50)
print("TYPE CASTING - LIMITATIONS & ERRORS")
print("=" * 50)

# ❌ String float to int directly - FAILS
try:
    z = '10.5'
    z_int = int(z)
    print(f"String float to int: '{z}' -> {z_int}")
except ValueError as e:
    print(f"❌ ERROR: Cannot convert '{z}' directly to int")
    print(f"   Reason: {e}")
    # Solution: Convert to float first, then to int
    z_int = int(float(z))
    print(f"✅ SOLUTION: '{z}' -> float({float(z)}) -> int({z_int})")

print()

# ❌ Non-numeric string to int - FAILS
try:
    a = 'hello'
    a_int = int(a)
    print(f"String to int: '{a}' -> {a_int}")
except ValueError as e:
    print(f"❌ ERROR: Cannot convert '{a}' to int")
    print(f"   Reason: {e}")

print()

# ❌ String with spaces to int - FAILS (unless stripped)
try:
    b = '  42  '
    b_int = int(b.strip())  # strip() removes whitespace
    print(f"✅ String with spaces: '{b}' -> {b_int} (after strip())")
except ValueError as e:
    print(f"❌ ERROR: {e}")

print()

# ❌ Empty string to int - FAILS
try:
    c = ''
    c_int = int(c)
except ValueError as e:
    print(f"❌ ERROR: Cannot convert empty string to int")
    print(f"   Reason: {e}")

print()

# ❌ None to int - FAILS
try:
    d = None
    d_int = int(d)
except TypeError as e:
    print(f"❌ ERROR: Cannot convert None to int")
    print(f"   Reason: {e}")

print()

# ============================================
# 4. TYPE HINTING (Python 3.5+)
# ============================================

print("=" * 50)
print("TYPE HINTING")
print("=" * 50)


def greet(name: str) -> str:
    """Function with type hints"""
    return f"Hello, {name}!"


def add_numbers(a: int, b: int) -> int:
    """Add two integers"""
    return a + b


def calculate_price(quantity: int, price: float) -> float:
    """Calculate total price"""
    return quantity * price


# Using the type-hinted functions
result1 = greet("Ragul")
result2 = add_numbers(10, 20)
result3 = calculate_price(5, 99.99)

print(f"greet('Ragul') -> {result1}")
print(f"add_numbers(10, 20) -> {result2}")
print(f"calculate_price(5, 99.99) -> {result3}")

print()

# Type hints for variables (Python 3.6+)
username: str = "ragul-143"
user_age: int = 25
user_balance: float = 1000.50
is_premium: bool = True
tags: list[str] = ["python", "coding", "learning"]

print(f"username: {username} (type hint: str)")
print(f"user_age: {user_age} (type hint: int)")
print(f"user_balance: {user_balance} (type hint: float)")
print(f"is_premium: {is_premium} (type hint: bool)")
print(f"tags: {tags} (type hint: list[str])")

print()

# ============================================
# 5. SAFE TYPE CASTING HELPER FUNCTIONS
# ============================================

print("=" * 50)
print("SAFE TYPE CASTING HELPERS")
print("=" * 50)


def safe_int(value, default=0):
    """Safely convert to int, return default if fails"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def safe_float(value, default=0.0):
    """Safely convert to float, return default if fails"""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


# Testing safe conversion functions
test_values = ['42', '3.14', 'hello', None, '', '  100  ']

print("Testing safe_int():")
for val in test_values:
    result = safe_int(val)
    print(f"  safe_int({repr(val)}) -> {result}")

print("\nTesting safe_float():")
for val in test_values:
    result = safe_float(val)
    print(f"  safe_float({repr(val)}) -> {result}")

print()
print("=" * 50)
print("DEMONSTRATION COMPLETE")
print("=" * 50)
