# ============================================
# COMPARISON OPERATORS (Relational Operators)
# ============================================

print("=" * 50)
print("COMPARISON OPERATORS")
print("=" * 50)

a = 10
b = 20

print(f"\na = {a}, b = {b}\n")

# Equal to (==)
result = a == b
print(f"{a} == {b} → {result}")

# Not equal to (!=)
result = a != b
print(f"{a} != {b} → {result}")

# Greater than (>)
result = a > b
print(f"{a} > {b} → {result}")

# Less than (<)
result = a < b
print(f"{a} < {b} → {result}")

# Greater than or equal to (>=)
result = a >= b
print(f"{a} >= {b} → {result}")

# Less than or equal to (<=)
result = a <= b
print(f"{a} <= {b} → {result}")

print()

# Practical Examples
print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Age verification
age = 17
if age >= 18:
    print(f"\nAge {age}: You can vote! ✅")
else:
    print(f"\nAge {age}: You cannot vote yet. ❌")

# Password length check
password = "secret123"
min_length = 8
if len(password) >= min_length:
    print(f"Password length {len(password)}: Valid ✅")
else:
    print(f"Password length {len(password)}: Too short ❌")

# Price comparison
original_price = 999
sale_price = 799
if sale_price < original_price:
    discount = original_price - sale_price
    print(f"\nDiscount available! Save ₹{discount}")

# String comparison
username = "ragul"
if username == "ragul":
    print(f"\nWelcome back, {username}! 👋")

print()
