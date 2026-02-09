# ============================================
# EXCEPTION HANDLING - PRACTICAL EXAMPLES
# ============================================

print("=" * 60)
print("EXCEPTION HANDLING - PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: User input validation
print("\n1️⃣  USER INPUT VALIDATION")
print("-" * 60)

def get_age():
    """Get valid age from user"""
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 120:
                raise ValueError("Age must be between 0 and 120")
            return age
        except ValueError as e:
            print(f"❌ Invalid input: {e}")
            print("Please try again.")

# Simulate with predefined input
print("Simulating age input...")
def simulate_age_input():
    try:
        age = int("25")
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120")
        print(f"✅ Age entered: {age}")
        return age
    except ValueError as e:
        print(f"❌ Invalid input: {e}")

simulate_age_input()

# Example 2: File operations with error handling
print("\n2️⃣  FILE OPERATIONS")
print("-" * 60)

def read_file_safely(filename):
    """Read file with proper error handling"""
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found")
        return None
    except PermissionError:
        print(f"❌ Permission denied for '{filename}'")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

# Test
content = read_file_safely("nonexistent.txt")
if content:
    print(content)

# Example 3: API request simulation
print("\n3️⃣  API REQUEST SIMULATION")
print("-" * 60)

class APIError(Exception):
    """Custom API exception"""
    pass

def fetch_user_data(user_id):
    """Simulate API request"""
    try:
        if user_id <= 0:
            raise ValueError("User ID must be positive")
        if user_id > 100:
            raise APIError("User not found")
        
        # Simulate successful response
        return {"id": user_id, "name": f"User{user_id}"}
    
    except ValueError as e:
        print(f"❌ Validation error: {e}")
        return None
    except APIError as e:
        print(f"❌ API error: {e}")
        return None

print(f"User data: {fetch_user_data(50)}")
print(f"User data: {fetch_user_data(-1)}")
print(f"User data: {fetch_user_data(200)}")

# Example 4: Database connection simulation
print("\n4️⃣  DATABASE CONNECTION")
print("-" * 60)

class DatabaseError(Exception):
    """Custom database exception"""
    pass

class Database:
    def __init__(self):
        self.connected = False
    
    def connect(self):
        """Simulate database connection"""
        try:
            # Simulate connection
            self.connected = True
            print("✅ Database connected")
        except Exception as e:
            raise DatabaseError(f"Connection failed: {e}")
    
    def query(self, sql):
        """Execute query"""
        if not self.connected:
            raise DatabaseError("Not connected to database")
        print(f"✅ Executing: {sql}")
        return []
    
    def close(self):
        """Close connection"""
        self.connected = False
        print("✅ Database connection closed")

# Usage with error handling
db = Database()
try:
    db.connect()
    db.query("SELECT * FROM users")
except DatabaseError as e:
    print(f"❌ Database error: {e}")
finally:
    db.close()

# Example 5: Calculator with error handling
print("\n5️⃣  CALCULATOR")
print("-" * 60)

class Calculator:
    """Calculator with error handling"""
    
    @staticmethod
    def divide(a, b):
        try:
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("Both arguments must be numbers")
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        except (TypeError, ZeroDivisionError) as e:
            print(f"❌ Error: {e}")
            return None
    
    @staticmethod
    def sqrt(n):
        try:
            if not isinstance(n, (int, float)):
                raise TypeError("Argument must be a number")
            if n < 0:
                raise ValueError("Cannot calculate square root of negative number")
            return n ** 0.5
        except (TypeError, ValueError) as e:
            print(f"❌ Error: {e}")
            return None

calc = Calculator()
print(f"10 / 2 = {calc.divide(10, 2)}")
print(f"10 / 0 = {calc.divide(10, 0)}")
print(f"sqrt(16) = {calc.sqrt(16)}")
print(f"sqrt(-4) = {calc.sqrt(-4)}")

# Example 6: JSON parsing
print("\n6️⃣  JSON PARSING")
print("-" * 60)

import json

def parse_json(json_string):
    """Parse JSON with error handling"""
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return None

# Valid JSON
valid_json = '{"name": "Ragul", "age": 25}'
print(f"✅ Parsed: {parse_json(valid_json)}")

# Invalid JSON
invalid_json = '{"name": "Ragul", age: 25}'  # Missing quotes
print(f"Parsed: {parse_json(invalid_json)}")

# Example 7: List operations
print("\n7️⃣  LIST OPERATIONS")
print("-" * 60)

def safe_get(lst, index, default=None):
    """Get item from list safely"""
    try:
        return lst[index]
    except IndexError:
        print(f"❌ Index {index} out of range")
        return default
    except TypeError:
        print(f"❌ Invalid index type")
        return default

numbers = [1, 2, 3, 4, 5]
print(f"Index 2: {safe_get(numbers, 2)}")
print(f"Index 10: {safe_get(numbers, 10, default='Not found')}")

# Example 8: Context manager with error handling
print("\n8️⃣  CONTEXT MANAGER")
print("-" * 60)

class FileManager:
    """Custom file manager with error handling"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except FileNotFoundError:
            print(f"❌ File '{self.filename}' not found")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print("✅ File closed")
        
        if exc_type is not None:
            print(f"❌ Error occurred: {exc_val}")
        
        return False  # Don't suppress exceptions

# Usage
try:
    with FileManager("test.txt", "w") as f:
        f.write("Hello, World!")
    print("✅ File written successfully")
except Exception as e:
    print(f"❌ Operation failed: {e}")

# Cleanup
import os
if os.path.exists("test.txt"):
    os.remove("test.txt")

# Example 9: Retry mechanism
print("\n9️⃣  RETRY MECHANISM")
print("-" * 60)

def retry_operation(func, max_attempts=3):
    """Retry function on failure"""
    for attempt in range(1, max_attempts + 1):
        try:
            result = func()
            print(f"✅ Success on attempt {attempt}")
            return result
        except Exception as e:
            print(f"❌ Attempt {attempt} failed: {e}")
            if attempt == max_attempts:
                print("❌ All attempts failed")
                raise

# Simulate operation that fails twice then succeeds
attempt_count = 0
def unreliable_operation():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ConnectionError("Network error")
    return "Success!"

try:
    result = retry_operation(unreliable_operation)
    print(f"Final result: {result}")
except Exception as e:
    print(f"Operation failed: {e}")

# Example 10: Validation decorator
print("\n🔟 VALIDATION DECORATOR")
print("-" * 60)

def validate_positive(func):
    """Decorator to validate positive numbers"""
    def wrapper(n):
        try:
            if n <= 0:
                raise ValueError("Number must be positive")
            return func(n)
        except ValueError as e:
            print(f"❌ Validation error: {e}")
            return None
    return wrapper

@validate_positive
def calculate_discount(price):
    """Calculate 10% discount"""
    return price * 0.9

print(f"Discount on ₹100: ₹{calculate_discount(100)}")
print(f"Discount on ₹-50: {calculate_discount(-50)}")

print()
