# ============================================
# FUNCTION SCOPE & VARIABLES
# ============================================

print("=" * 60)
print("FUNCTION SCOPE & VARIABLES")
print("=" * 60)

# Local variables
print("\n1️⃣  LOCAL VARIABLES")
print("-" * 60)

def calculate():
    """Variables inside function are local"""
    x = 10  # Local variable
    y = 20  # Local variable
    result = x + y
    print(f"Inside function: x={x}, y={y}, result={result}")

calculate()
# print(x)  # ❌ Error: x is not defined outside function

# Global variables
print("\n2️⃣  GLOBAL VARIABLES")
print("-" * 60)

counter = 0  # Global variable

def increment():
    """Reading global variable"""
    print(f"Counter: {counter}")

increment()
print(f"Global counter: {counter}")

# Modifying global variables
print("\n3️⃣  MODIFYING GLOBAL VARIABLES")
print("-" * 60)

total = 0  # Global variable

def add_to_total(amount):
    """Modify global variable using 'global' keyword"""
    global total
    total += amount
    print(f"Added {amount}, Total: {total}")

add_to_total(10)
add_to_total(20)
print(f"Final total: {total}")

# Nonlocal variables (nested functions)
print("\n4️⃣  NONLOCAL VARIABLES")
print("-" * 60)

def outer():
    """Outer function"""
    count = 0  # Enclosing variable
    
    def inner():
        """Inner function"""
        nonlocal count  # Access enclosing variable
        count += 1
        print(f"Count: {count}")
    
    inner()
    inner()
    inner()

outer()

# Return vs Print
print("\n5️⃣  RETURN VS PRINT")
print("-" * 60)

def print_sum(a, b):
    """Prints but doesn't return"""
    print(a + b)

def return_sum(a, b):
    """Returns the value"""
    return a + b

print("Using print_sum:")
result1 = print_sum(5, 3)  # Prints 8
print(f"Result: {result1}")  # None

print("\nUsing return_sum:")
result2 = return_sum(5, 3)  # Returns 8
print(f"Result: {result2}")  # 8

print()
