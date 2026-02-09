# ============================================
# FOR LOOPS
# ============================================

print("=" * 60)
print("FOR LOOPS")
print("=" * 60)

# Loop through a list
print("\n1️⃣  LOOP THROUGH LIST")
print("-" * 60)
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Loop through a string
print("\n2️⃣  LOOP THROUGH STRING")
print("-" * 60)
for char in "Python":
    print(char, end=" ")
print()

# Loop with range()
print("\n3️⃣  LOOP WITH RANGE")
print("-" * 60)
# range(stop)
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# range(start, stop)
for i in range(2, 6):
    print(i, end=" ")  # 2 3 4 5
print()

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8
print()

# Loop with enumerate (index + value)
print("\n4️⃣  ENUMERATE (Index + Value)")
print("-" * 60)
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")

# Loop through dictionary
print("\n5️⃣  LOOP THROUGH DICTIONARY")
print("-" * 60)
user = {"name": "Ragul", "age": 25, "city": "Chennai"}

# Keys only
for key in user:
    print(f"Key: {key}")

# Values only
for value in user.values():
    print(f"Value: {value}")

# Key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")

# Nested loops
print("\n6️⃣  NESTED LOOPS")
print("-" * 60)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()

# List comprehension (compact for loop)
print("\n7️⃣  LIST COMPREHENSION")
print("-" * 60)
# Normal loop
squares = []
for i in range(5):
    squares.append(i ** 2)
print(f"Squares (normal): {squares}")

# List comprehension (one line)
squares = [i ** 2 for i in range(5)]
print(f"Squares (comprehension): {squares}")

# With condition
evens = [i for i in range(10) if i % 2 == 0]
print(f"Even numbers: {evens}")

print()
