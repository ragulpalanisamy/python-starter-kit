# ============================================
# CLASSES WITHOUT CONSTRUCTORS
# ============================================

print("=" * 60)
print("CLASSES WITHOUT CONSTRUCTORS")
print("=" * 60)

# Simple class without constructor
print("\n1️⃣  SIMPLE CLASS (No Constructor)")
print("-" * 60)

class MathUtils:
    """Utility class - no need for constructor"""
    
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

math = MathUtils()
print(f"5 + 3 = {math.add(5, 3)}")
print(f"5 × 3 = {math.multiply(5, 3)}")

# Class with only static methods
print("\n2️⃣  STATIC METHODS ONLY (No Constructor)")
print("-" * 60)

class StringHelper:
    """Helper class with static methods"""
    
    @staticmethod
    def reverse(text):
        return text[::-1]
    
    @staticmethod
    def capitalize_words(text):
        return text.title()
    
    @staticmethod
    def count_vowels(text):
        return sum(1 for c in text.lower() if c in 'aeiou')

# No need to create instance
print(f"Reverse: {StringHelper.reverse('hello')}")
print(f"Capitalize: {StringHelper.capitalize_words('hello world')}")
print(f"Vowels: {StringHelper.count_vowels('hello')}")

# Class with only class methods
print("\n3️⃣  CLASS METHODS ONLY (No Constructor)")
print("-" * 60)

class Config:
    """Configuration class"""
    
    app_name = "MyApp"
    version = "1.0.0"
    
    @classmethod
    def get_info(cls):
        return f"{cls.app_name} v{cls.version}"
    
    @classmethod
    def update_version(cls, new_version):
        cls.version = new_version

print(f"Info: {Config.get_info()}")
Config.update_version("2.0.0")
print(f"Updated: {Config.get_info()}")

# Setting attributes after creation
print("\n4️⃣  SETTING ATTRIBUTES AFTER CREATION")
print("-" * 60)

class Person:
    """Class without constructor"""
    
    def greet(self):
        return f"Hello, I'm {self.name}"

# Create instance and set attributes manually
person = Person()
person.name = "Ragul"
person.age = 25
print(person.greet())
print(f"Age: {person.age}")

# Empty class (placeholder)
print("\n5️⃣  EMPTY CLASS (Placeholder)")
print("-" * 60)

class DataContainer:
    """Empty class used as data container"""
    pass

# Use as flexible data container
data = DataContainer()
data.username = "ragul"
data.email = "ragul@example.com"
data.active = True

print(f"Username: {data.username}")
print(f"Email: {data.email}")
print(f"Active: {data.active}")

# Constants class
print("\n6️⃣  CONSTANTS CLASS (No Constructor)")
print("-" * 60)

class Colors:
    """Color constants"""
    RED = "#FF0000"
    GREEN = "#00FF00"
    BLUE = "#0000FF"
    WHITE = "#FFFFFF"
    BLACK = "#000000"

print(f"Red: {Colors.RED}")
print(f"Blue: {Colors.BLUE}")

# Namespace class
print("\n7️⃣  NAMESPACE CLASS (No Constructor)")
print("-" * 60)

class API:
    """API endpoints namespace"""
    
    class Users:
        LIST = "/api/users"
        CREATE = "/api/users/create"
        DELETE = "/api/users/delete"
    
    class Products:
        LIST = "/api/products"
        CREATE = "/api/products/create"

print(f"Users list: {API.Users.LIST}")
print(f"Products create: {API.Products.CREATE}")

# When constructor IS useful
print("\n8️⃣  WHEN CONSTRUCTOR IS USEFUL")
print("-" * 60)

class BankAccount:
    """Constructor needed for initialization"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

account = BankAccount("Ragul", 1000)
print(f"Owner: {account.owner}")
print(f"Balance: ₹{account.balance}")

print("\n✅ Use constructor when:")
print("  - You need to initialize attributes")
print("  - You need to validate input")
print("  - You need to set up initial state")

print("\n❌ Constructor NOT needed when:")
print("  - Only using static/class methods")
print("  - Creating utility/helper classes")
print("  - Defining constants")
print("  - Using class as namespace")

print()
