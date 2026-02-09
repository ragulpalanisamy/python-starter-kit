# ============================================
# LIST OPERATIONS & TECHNIQUES
# ============================================

print("=" * 60)
print("LIST OPERATIONS & TECHNIQUES")
print("=" * 60)

# List comprehension
print("\n1️⃣  LIST COMPREHENSION")
print("-" * 60)

# Basic comprehension
squares = [x ** 2 for x in range(5)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Transform strings
fruits = ["apple", "banana", "mango"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(f"Uppercase: {upper_fruits}")

# Nested loops
pairs = [(x, y) for x in range(3) for y in range(3)]
print(f"Pairs: {pairs}")

# Iterating through lists
print("\n2️⃣  ITERATING THROUGH LISTS")
print("-" * 60)

# Simple iteration
fruits = ["apple", "banana", "mango"]
print("Using for loop:")
for fruit in fruits:
    print(f"  {fruit}")

# With index using enumerate
print("\nWith enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# With custom start index
print("\nWith custom start:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# Unpacking lists
print("\n3️⃣  UNPACKING LISTS")
print("-" * 60)

# Basic unpacking
numbers = [1, 2, 3]
a, b, c = numbers
print(f"Numbers: {numbers}")
print(f"a={a}, b={b}, c={c}")

# Extended unpacking
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"Numbers: {numbers}")
print(f"first={first}, middle={middle}, last={last}")

# Nested lists
print("\n4️⃣  NESTED LISTS (2D Lists)")
print("-" * 60)

# Create 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Access elements
print(f"\nElement at [0][0]: {matrix[0][0]}")
print(f"Element at [1][2]: {matrix[1][2]}")

# Flatten nested list
flat = [item for row in matrix for item in row]
print(f"Flattened: {flat}")

# Finding min/max
print("\n5️⃣  MIN/MAX/SUM")
print("-" * 60)
numbers = [45, 23, 89, 12, 67]
print(f"Numbers: {numbers}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")

# Filtering lists
print("\n6️⃣  FILTERING LISTS")
print("-" * 60)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")

# Using filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens (filter): {evens}")

# Using comprehension
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens (comprehension): {evens}")

# Mapping lists
print("\n7️⃣  MAPPING LISTS")
print("-" * 60)
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Using map()
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared (map): {squared}")

# Using comprehension
squared = [x ** 2 for x in numbers]
print(f"Squared (comprehension): {squared}")

# Zipping lists
print("\n8️⃣  ZIPPING LISTS")
print("-" * 60)
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

# Combine lists
combined = list(zip(names, ages, cities))
print(f"Names: {names}")
print(f"Ages: {ages}")
print(f"Cities: {cities}")
print(f"Zipped: {combined}")

# Iterate over zipped
print("\nIterate over zipped:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}, {city}")

# Removing duplicates
print("\n9️⃣  REMOVING DUPLICATES")
print("-" * 60)
numbers = [1, 2, 3, 2, 4, 3, 5, 1]
print(f"Original: {numbers}")

# Using set (loses order)
unique = list(set(numbers))
print(f"Unique (set): {unique}")

# Preserving order
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(f"Unique (preserving order): {unique}")

# Using dict.fromkeys (preserves order in Python 3.7+)
unique = list(dict.fromkeys(numbers))
print(f"Unique (dict.fromkeys): {unique}")

print()
