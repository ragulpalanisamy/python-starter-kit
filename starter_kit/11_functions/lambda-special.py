# ============================================
# LAMBDA FUNCTIONS & SPECIAL FUNCTIONS
# ============================================

print("=" * 60)
print("LAMBDA FUNCTIONS & SPECIAL FUNCTIONS")
print("=" * 60)

# Lambda functions (anonymous functions)
print("\n1️⃣  LAMBDA FUNCTIONS")
print("-" * 60)

# Regular function
def square(x):
    return x ** 2

# Lambda equivalent (one line)
square_lambda = lambda x: x ** 2

print(f"Regular: square(5) = {square(5)}")
print(f"Lambda: square_lambda(5) = {square_lambda(5)}")

# Lambda with multiple parameters
add = lambda a, b: a + b
print(f"Lambda add: {add(10, 5)}")

# Lambda in sorting
print("\n2️⃣  LAMBDA WITH SORTING")
print("-" * 60)

students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 23}
]

# Sort by age using lambda
sorted_students = sorted(students, key=lambda x: x["age"])
print("Sorted by age:")
for student in sorted_students:
    print(f"  {student['name']}: {student['age']}")

# map() - Apply function to all items
print("\n3️⃣  MAP() FUNCTION")
print("-" * 60)

numbers = [1, 2, 3, 4, 5]

# Square all numbers
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# filter() - Filter items based on condition
print("\n4️⃣  FILTER() FUNCTION")
print("-" * 60)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Original: {numbers}")
print(f"Evens: {evens}")

# reduce() - Reduce to single value
print("\n5️⃣  REDUCE() FUNCTION")
print("-" * 60)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Calculate product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(f"Numbers: {numbers}")
print(f"Product: {product}")

# Recursive functions
print("\n6️⃣  RECURSIVE FUNCTIONS")
print("-" * 60)

def factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")  # 5! = 120
print(f"Factorial of 3: {factorial(3)}")  # 3! = 6

# Fibonacci using recursion
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci sequence (first 10):")
for i in range(10):
    print(fibonacci(i), end=" ")
print()

print()
