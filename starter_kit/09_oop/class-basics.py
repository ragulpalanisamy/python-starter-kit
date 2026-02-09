# ============================================
# CLASS BASICS
# ============================================

print("=" * 60)
print("CLASS BASICS - Introduction to OOP")
print("=" * 60)

# Simple class
print("\n1️⃣  SIMPLE CLASS")
print("-" * 60)

class Dog:
    """A simple Dog class"""
    pass

# Create object (instance)
my_dog = Dog()
print(f"Created dog object: {my_dog}")

# Class with attributes
print("\n2️⃣  CLASS WITH ATTRIBUTES")
print("-" * 60)

class Person:
    """Person class with attributes"""
    
    def __init__(self, name, age):
        """Constructor - runs when object is created"""
        self.name = name  # Instance attribute
        self.age = age

# Create objects
person1 = Person("Ragul", 25)
person2 = Person("Alice", 30)

print(f"Person 1: {person1.name}, Age: {person1.age}")
print(f"Person 2: {person2.name}, Age: {person2.age}")

# Class with methods
print("\n3️⃣  CLASS WITH METHODS")
print("-" * 60)

class Calculator:
    """Calculator class with methods"""
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        return a - b

calc = Calculator()
print(f"10 + 5 = {calc.add(10, 5)}")
print(f"10 - 5 = {calc.subtract(10, 5)}")

# Complete class example
print("\n4️⃣  COMPLETE CLASS EXAMPLE")
print("-" * 60)

class BankAccount:
    """Bank account class"""
    
    def __init__(self, owner, balance=0):
        """Initialize account"""
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money"""
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
    
    def withdraw(self, amount):
        """Withdraw money"""
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
    
    def get_balance(self):
        """Get current balance"""
        return self.balance

# Create account
account = BankAccount("Ragul", 1000)
print(f"Account owner: {account.owner}")
print(f"Initial balance: ₹{account.get_balance()}")

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Insufficient funds

# Class vs Instance attributes
print("\n5️⃣  CLASS VS INSTANCE ATTRIBUTES")
print("-" * 60)

class Student:
    """Student class"""
    
    # Class attribute (shared by all instances)
    school = "ABC School"
    
    def __init__(self, name, grade):
        # Instance attributes (unique to each instance)
        self.name = name
        self.grade = grade

student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

print(f"Student 1: {student1.name}, Grade: {student1.grade}, School: {student1.school}")
print(f"Student 2: {student2.name}, Grade: {student2.grade}, School: {student2.school}")

# Change class attribute
Student.school = "XYZ School"
print(f"\nAfter changing school:")
print(f"Student 1 school: {student1.school}")
print(f"Student 2 school: {student2.school}")

# String representation
print("\n6️⃣  STRING REPRESENTATION (__str__ and __repr__)")
print("-" * 60)

class Book:
    """Book class with string representation"""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        """User-friendly string representation"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Book(title='{self.title}', author='{self.author}')"

book = Book("Python Basics", "John Doe")
print(f"Using print: {book}")  # Calls __str__
print(f"Using repr: {repr(book)}")  # Calls __repr__

print()
