# ============================================
# LOOP CONTROL - BREAK, CONTINUE, PASS
# ============================================

print("=" * 60)
print("LOOP CONTROL STATEMENTS")
print("=" * 60)

# BREAK - Exit the loop
print("\n1️⃣  BREAK - Exit Loop")
print("-" * 60)
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(i, end=" ")
print()

# CONTINUE - Skip current iteration
print("\n2️⃣  CONTINUE - Skip Iteration")
print("-" * 60)
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i, end=" ")  # Only odd numbers printed
print()

# PASS - Do nothing (placeholder)
print("\n3️⃣  PASS - Placeholder")
print("-" * 60)
for i in range(5):
    if i == 2:
        pass  # TODO: Add logic here later
    print(i, end=" ")
print()

# Practical examples
print("\n4️⃣  PRACTICAL EXAMPLES")
print("-" * 60)

# Example 1: Find first even number
print("\nFind first even number:")
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even: {num}")
        break

# Example 2: Skip negative numbers
print("\nSkip negative numbers:")
values = [5, -2, 8, -1, 3]
for val in values:
    if val < 0:
        continue
    print(val, end=" ")
print()

# Example 3: Search in nested loop
print("\nSearch in 2D list:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5
found = False

for row in matrix:
    for num in row:
        if num == target:
            print(f"Found {target}!")
            found = True
            break
    if found:
        break

print()
