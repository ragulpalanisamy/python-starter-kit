# ============================================
# FUNCTION ARGUMENTS
# ============================================

print("=" * 60)
print("FUNCTION ARGUMENTS")
print("=" * 60)

# Positional arguments
print("\n1️⃣  POSITIONAL ARGUMENTS")
print("-" * 60)

def create_profile(name, age, city):
    """Arguments passed by position"""
    print(f"Name: {name}, Age: {age}, City: {city}")

create_profile("Ragul", 25, "Chennai")

# Keyword arguments
print("\n2️⃣  KEYWORD ARGUMENTS")
print("-" * 60)

def create_profile(name, age, city):
    """Arguments passed by name"""
    print(f"Name: {name}, Age: {age}, City: {city}")

create_profile(city="Chennai", name="Ragul", age=25)  # Order doesn't matter

# Mixed positional and keyword
print("\n3️⃣  MIXED ARGUMENTS")
print("-" * 60)

create_profile("Ragul", age=25, city="Chennai")  # Positional first, then keyword

# Default arguments
print("\n4️⃣  DEFAULT ARGUMENTS")
print("-" * 60)

def create_user(name, role="User", active=True):
    """Function with default values"""
    print(f"Name: {name}, Role: {role}, Active: {active}")

create_user("Ragul")                           # Uses all defaults
create_user("Alice", "Admin")                  # Overrides role
create_user("Bob", active=False)               # Overrides active only

# *args - Variable positional arguments
print("\n5️⃣  *ARGS (Variable Positional)")
print("-" * 60)

def sum_all(*numbers):
    """Accept any number of positional arguments"""
    total = sum(numbers)
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")

sum_all(1, 2, 3)
sum_all(10, 20, 30, 40, 50)

# **kwargs - Variable keyword arguments
print("\n6️⃣  **KWARGS (Variable Keyword)")
print("-" * 60)

def display_info(**info):
    """Accept any number of keyword arguments"""
    print("User Information:")
    for key, value in info.items():
        print(f"  {key}: {value}")

display_info(name="Ragul", age=25, city="Chennai")
display_info(name="Alice", role="Admin", email="alice@example.com")

# Combining all argument types
print("\n7️⃣  COMBINING ALL TYPES")
print("-" * 60)

def create_order(item, quantity, *extras, discount=0, **details):
    """
    Combines all argument types:
    - item: positional
    - quantity: positional
    - *extras: variable positional
    - discount: keyword with default
    - **details: variable keyword
    """
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Extras: {extras}")
    print(f"Discount: {discount}%")
    print(f"Details: {details}")

create_order("Pizza", 2, "Cheese", "Olives", discount=10, delivery="Express", payment="Card")

print()
