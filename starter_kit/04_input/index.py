# ============================================
# USER INPUT IN PYTHON
# ============================================

print("=" * 60)
print("USER INPUT METHODS IN PYTHON")
print("=" * 60)

# ============================================
# 1. BASIC INPUT - input() function
# ============================================

print("\n1️⃣  BASIC INPUT")
print("-" * 60)

# NOTE: input() always returns a STRING
name = input("Enter your name: ")
print(f"Hello, {name}!")
print(f"Type of input: {type(name)}")

print()

# ============================================
# 2. INPUT WITH TYPE CASTING
# ============================================

print("2️⃣  INPUT WITH TYPE CASTING")
print("-" * 60)

# Converting string input to integer
age = int(input("Enter your age: "))
print(f"You are {age} years old")
print(f"Type: {type(age)}")

# Converting string input to float
height = float(input("Enter your height in meters: "))
print(f"Your height is {height}m")
print(f"Type: {type(height)}")

print()

# ============================================
# 3. MULTIPLE INPUTS (Using split())
# ============================================

print("3️⃣  MULTIPLE INPUTS")
print("-" * 60)

# Split by space (default)
print("Enter your first name and last name (separated by space):")
first_name, last_name = input().split()
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")

# Split with custom separator
print("\nEnter three numbers separated by commas:")
a, b, c = input().split(',')
print(f"Numbers: {a}, {b}, {c}")

# Split and convert to integers
print("\nEnter three numbers separated by spaces:")
nums = list(map(int, input().split()))
print(f"Numbers as integers: {nums}")
print(f"Sum: {sum(nums)}")

print()

# ============================================
# 4. ERROR HANDLING
# ============================================

print("4️⃣  ERROR HANDLING")
print("-" * 60)

# Safe integer input
try:
    user_age = int(input("Enter your age: "))
    print(f"✅ Valid age: {user_age}")
except ValueError:
    print("❌ Invalid input! Please enter a valid number.")

# Safe float input with retry
while True:
    try:
        price = float(input("Enter price: "))
        print(f"✅ Price: ₹{price}")
        break
    except ValueError:
        print("❌ Invalid! Please enter a valid number.")

print()

# ============================================
# 5. INPUT VALIDATION
# ============================================

print("5️⃣  INPUT VALIDATION")
print("-" * 60)

# Validate non-empty input
username = input("Enter username: ").strip()
if username:
    print(f"✅ Username: {username}")
else:
    print("❌ Username cannot be empty!")

# Validate email format
email = input("Enter email: ")
if "@" in email and "." in email:
    print(f"✅ Email looks valid: {email}")
else:
    print(f"❌ Invalid email format!")

# Validate age range
try:
    age_check = int(input("Enter your age: "))
    if 0 < age_check < 120:
        print(f"✅ Valid age: {age_check}")
    else:
        print(f"❌ Age must be between 1 and 119!")
except ValueError:
    print("❌ Please enter a valid number!")

print()

# ============================================
# 6. COMMAND-LINE ARGUMENTS (sys.argv)
# ============================================

print("6️⃣  COMMAND-LINE ARGUMENTS")
print("-" * 60)

import sys

print(f"Script name: {sys.argv[0]}")
print(f"Total arguments: {len(sys.argv)}")
print(f"All arguments: {sys.argv}")

# Check if arguments were provided
if len(sys.argv) > 1:
    full_name = sys.argv[1]
    print(f"\n✅ Hello, {full_name}!")
    
    # Generate company email
    email = full_name.lower().replace(" ", "") + "@company.com"
    print(f"📧 Company Email: {email}")
else:
    print("\n⚠️  No name provided as command-line argument")
    print("Usage: python3 index.py 'Your Name'")

# Access multiple arguments
if len(sys.argv) > 2:
    print(f"\nAdditional arguments:")
    for i, arg in enumerate(sys.argv[2:], start=2):
        print(f"  argv[{i}]: {arg}")

print()

# ============================================
# 7. OTHER INPUT METHODS
# ============================================

print("7️⃣  OTHER INPUT METHODS")
print("-" * 60)

# Method 1: sys.stdin.readline()
print("\nMethod 1: Using sys.stdin.readline()")
print("Enter a line: ", end="")
line = sys.stdin.readline().strip()
print(f"You entered: {line}")

# Method 2: getpass (for password input - hidden)
print("\nMethod 2: Using getpass (hidden input)")
from getpass import getpass
password = getpass("Enter password: ")
print(f"Password length: {len(password)} characters")

print()

# ============================================
# 8. PRACTICAL EXAMPLES
# ============================================

print("8️⃣  PRACTICAL EXAMPLES")
print("-" * 60)

# Example 1: Simple Calculator
print("\n📊 Simple Calculator")
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operation"
    
    print(f"Result: {result}")
except ValueError:
    print("❌ Invalid number input!")
except Exception as e:
    print(f"❌ Error: {e}")

# Example 2: User Registration
print("\n👤 User Registration")
user_data = {
    "username": input("Username: ").strip(),
    "email": input("Email: ").strip(),
    "age": input("Age: ").strip()
}

print("\n✅ Registration Summary:")
for key, value in user_data.items():
    print(f"  {key.capitalize()}: {value}")

print()
print("=" * 60)
print("✅ INPUT DEMONSTRATION COMPLETE")
print("=" * 60)
