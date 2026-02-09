# ============================================
# TUPLE BASICS
# ============================================

print("=" * 60)
print("TUPLE BASICS")
print("=" * 60)

# Creating tuples
print("\n1️⃣  CREATING TUPLES")
print("-" * 60)

# Empty tuple
empty = ()
print(f"Empty tuple: {empty}")

# Tuple with values
numbers = (1, 2, 3, 4, 5)
print(f"Numbers: {numbers}")

# Single element tuple (note the comma)
single = (5,)
print(f"Single element: {single}")

# Without parentheses
coordinates = 10, 20
print(f"Coordinates: {coordinates}")

# Mixed types
mixed = (1, "hello", 3.14, True)
print(f"Mixed: {mixed}")

# Accessing elements
print("\n2️⃣  ACCESSING ELEMENTS")
print("-" * 60)
fruits = ("apple", "banana", "mango")
print(f"Fruits: {fruits}")
print(f"First: {fruits[0]}")
print(f"Last: {fruits[-1]}")

# Slicing
print("\n3️⃣  SLICING")
print("-" * 60)
numbers = (0, 1, 2, 3, 4, 5)
print(f"Numbers: {numbers}")
print(f"[0:3]: {numbers[0:3]}")
print(f"[::2]: {numbers[::2]}")

# Tuple methods
print("\n4️⃣  TUPLE METHODS")
print("-" * 60)
numbers = (1, 2, 3, 2, 4, 2)
print(f"Numbers: {numbers}")
print(f"count(2): {numbers.count(2)}")
print(f"index(3): {numbers.index(3)}")

# Immutability
print("\n5️⃣  IMMUTABILITY")
print("-" * 60)
point = (10, 20)
print(f"Point: {point}")
# point[0] = 15  # ❌ Error: tuples are immutable
print("Tuples cannot be modified after creation")

# Unpacking
print("\n6️⃣  UNPACKING")
print("-" * 60)
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

print()
