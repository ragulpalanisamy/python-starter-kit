# ============================================
# ARITHMETIC OPERATORS
# ============================================

print("=" * 50)
print("ARITHMETIC OPERATORS")
print("=" * 50)

a = 20
b = 6

print(f"\na = {a}, b = {b}\n")

# Addition (+)
result = a + b
print(f"Addition: {a} + {b} = {result}")

# Subtraction (-)
result = a - b
print(f"Subtraction: {a} - {b} = {result}")

# Multiplication (*)
result = a * b
print(f"Multiplication: {a} * {b} = {result}")

# Division (/) - Always returns float
result = a / b
print(f"Division: {a} / {b} = {result}")

# Floor Division (//) - Returns integer (rounds down)
result = a // b
print(f"Floor Division: {a} // {b} = {result}")

# Modulus (%) - Returns remainder
result = a % b
print(f"Modulus: {a} % {b} = {result}")

# Exponentiation (**) - Power
result = a ** 2
print(f"Exponentiation: {a} ** 2 = {result}")

print()

# Practical Examples
print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Calculate total price
quantity = 5
price_per_item = 99.99
total = quantity * price_per_item
print(f"\nShopping: {quantity} items × ₹{price_per_item} = ₹{total}")

# Split bill equally
bill = 1500
people = 4
per_person = bill / people
print(f"Bill Split: ₹{bill} ÷ {people} people = ₹{per_person} per person")

# Check if number is even or odd
number = 17
if number % 2 == 0:
    print(f"\n{number} is EVEN")
else:
    print(f"\n{number} is ODD")

# Calculate area of circle
radius = 7
pi = 3.14159
area = pi * (radius ** 2)
print(f"\nCircle Area: π × {radius}² = {area:.2f}")

print()
