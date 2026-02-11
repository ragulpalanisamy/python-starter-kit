# ============================================
# LIST BASICS
# ============================================

print("=" * 60)
print("LIST BASICS")
print("=" * 60)

# Creating lists
print("\n1️⃣  CREATING LISTS")
print("-" * 60)

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with values
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Mixed data types
mixed = [1, "hello", 3.14, True, [1, 2]]
print(f"Mixed types: {mixed}")

# Using list() constructor
from_range = list(range(5))
print(f"From range: {from_range}")

from_string = list("Python")
print(f"From string: {from_string}")

# List length
print("\n2️⃣  LIST LENGTH")
print("-" * 60)
fruits = ["apple", "banana", "mango"]
print(f"Fruits: {fruits}")
print(f"Length: {len(fruits)}")

# Accessing elements (indexing)
print("\n3️⃣  ACCESSING ELEMENTS")
print("-" * 60)
colors = ["red", "green", "blue", "yellow"]
print(f"Colors: {colors}")
print(f"First element: {colors[0]}")
print(f"Last element: {colors[-1]}")
print(f"Second element: {colors[1]}")
print(f"Second from end: {colors[-2]}")

# Slicing
print("\n4️⃣  SLICING")
print("-" * 60)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Numbers: {numbers}")
print(f"[0:5]: {numbers[0:5]}")      # First 5
print(f"[5:]: {numbers[5:]}")        # From index 5 to end
print(f"[:5]: {numbers[:5]}")        # First 5
print(f"[::2]: {numbers[::2]}")      # Every 2nd element
print(f"[::-1]: {numbers[::-1]}")    # Reverse

# Checking membership
print("\n5️⃣  MEMBERSHIP")
print("-" * 60)
fruits = ["apple", "banana", "mango"]
print(f"Fruits: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'orange' in fruits: {'orange' in fruits}")
print(f"'banana' not in fruits: {'banana' not in fruits}")

# List concatenation
print("\n6️⃣  CONCATENATION")
print("-" * 60)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"Combined: {combined}")

# List repetition
print("\n7️⃣  REPETITION")
print("-" * 60)
pattern = [0, 1]
repeated = pattern * 3
print(f"Pattern: {pattern}")
print(f"Repeated 3 times: {repeated}")

print()
