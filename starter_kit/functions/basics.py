# ============================================
# FUNCTION BASICS
# ============================================

print("=" * 60)
print("FUNCTION BASICS")
print("=" * 60)

# Simple function (no parameters, no return)
print("\n1️⃣  SIMPLE FUNCTION")
print("-" * 60)

def greet():
    """Function without parameters"""
    print("Hello, World!")

greet()  # Call the function

# Function with parameters
print("\n2️⃣  FUNCTION WITH PARAMETERS")
print("-" * 60)

def greet_user(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

greet_user("Ragul")
greet_user("Alice")

# Function with multiple parameters
print("\n3️⃣  MULTIPLE PARAMETERS")
print("-" * 60)

def add_numbers(a, b):
    """Function with two parameters"""
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(10, 5)
add_numbers(100, 200)

# Function with return value
print("\n4️⃣  FUNCTION WITH RETURN")
print("-" * 60)

def multiply(a, b):
    """Function that returns a value"""
    return a * b

result = multiply(5, 3)
print(f"5 × 3 = {result}")

# Using return value in expression
total = multiply(10, 2) + multiply(5, 4)
print(f"Total: {total}")

# Function with default parameters
print("\n5️⃣  DEFAULT PARAMETERS")
print("-" * 60)

def greet_with_title(name, title="Mr."):
    """Function with default parameter"""
    print(f"Hello, {title} {name}!")

greet_with_title("Ragul")              # Uses default "Mr."
greet_with_title("Ragul", "Dr.")       # Overrides default

# Function with multiple return values
print("\n6️⃣  MULTIPLE RETURN VALUES")
print("-" * 60)

def get_user_info():
    """Function returning multiple values"""
    name = "Ragul"
    age = 25
    city = "Chennai"
    return name, age, city

name, age, city = get_user_info()
print(f"Name: {name}, Age: {age}, City: {city}")

# Docstring (function documentation)
print("\n7️⃣  DOCSTRING")
print("-" * 60)

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
    
    Returns:
        float: Area of the rectangle
    """
    return length * width

area = calculate_area(10, 5)
print(f"Area: {area}")
print(f"Docstring: {calculate_area.__doc__}")

print()
