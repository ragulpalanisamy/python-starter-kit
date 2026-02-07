# ============================================
# SET BASICS
# ============================================

print("=" * 60)
print("SET BASICS")
print("=" * 60)

# Creating sets
print("\n1️⃣  CREATING SETS")
print("-" * 60)

# Empty set (must use set())
empty = set()
print(f"Empty set: {empty}")

# Set with values
numbers = {1, 2, 3, 4, 5}
print(f"Numbers: {numbers}")

# From list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 4])
print(f"From list: {numbers}")

# Set operations
print("\n2️⃣  SET OPERATIONS")
print("-" * 60)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# Set methods
print("\n3️⃣  SET METHODS")
print("-" * 60)
fruits = {"apple", "banana"}
print(f"Original: {fruits}")
fruits.add("mango")
print(f"After add: {fruits}")
fruits.remove("banana")
print(f"After remove: {fruits}")

# Membership
print("\n4️⃣  MEMBERSHIP")
print("-" * 60)
print(f"'apple' in fruits: {'apple' in fruits}")

print()
