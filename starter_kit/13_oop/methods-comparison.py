# ============================================
# INSTANCE vs CLASS vs STATIC METHODS
# ============================================

print("=" * 60)
print("INSTANCE vs CLASS vs STATIC METHODS")
print("=" * 60)

# Instance Methods
print("\n1️⃣  INSTANCE METHODS")
print("-" * 60)
print("Access instance data (self)")

class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age
    
    def bark(self):
        """Instance method - uses self"""
        return f"{self.name} says Woof!"
    
    def get_age(self):
        """Instance method - accesses instance data"""
        return self.age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())  # Buddy says Woof!
print(dog2.bark())  # Max says Woof!
print(f"{dog1.name} is {dog1.get_age()} years old")

# Class Methods
print("\n2️⃣  CLASS METHODS")
print("-" * 60)
print("Access class data (cls)")

class Student:
    school = "ABC School"  # Class attribute
    student_count = 0
    
    def __init__(self, name):
        self.name = name
        Student.student_count += 1
    
    @classmethod
    def get_school(cls):
        """Class method - uses cls"""
        return cls.school
    
    @classmethod
    def change_school(cls, new_school):
        """Class method - modifies class attribute"""
        cls.school = new_school
    
    @classmethod
    def get_student_count(cls):
        """Class method - accesses class data"""
        return cls.student_count

# Call class method without creating instance
print(f"School: {Student.get_school()}")

# Create students
s1 = Student("Alice")
s2 = Student("Bob")

print(f"Total students: {Student.get_student_count()}")

# Change school for all students
Student.change_school("XYZ School")
print(f"New school: {Student.get_school()}")

# Static Methods
print("\n3️⃣  STATIC METHODS")
print("-" * 60)
print("No access to instance or class data")

class MathUtils:
    """Utility class with static methods"""
    
    @staticmethod
    def add(a, b):
        """Static method - no self or cls"""
        return a + b
    
    @staticmethod
    def is_even(num):
        """Static method - utility function"""
        return num % 2 == 0
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Static method - conversion"""
        return (celsius * 9/5) + 32

# Call static methods without creating instance
print(f"5 + 3 = {MathUtils.add(5, 3)}")
print(f"Is 10 even? {MathUtils.is_even(10)}")
print(f"25°C = {MathUtils.celsius_to_fahrenheit(25)}°F")

# Comparison Example
print("\n4️⃣  ALL THREE TOGETHER")
print("-" * 60)

class Employee:
    company = "TechCorp"  # Class attribute
    employee_count = 0
    
    def __init__(self, name, salary):
        self.name = name      # Instance attribute
        self.salary = salary
        Employee.employee_count += 1
    
    # Instance method
    def get_details(self):
        """Uses instance data (self)"""
        return f"{self.name} earns ₹{self.salary}"
    
    # Class method
    @classmethod
    def get_company(cls):
        """Uses class data (cls)"""
        return cls.company
    
    @classmethod
    def create_intern(cls, name):
        """Factory method - creates instance"""
        return cls(name, 20000)
    
    # Static method
    @staticmethod
    def is_valid_salary(salary):
        """Utility - no self or cls needed"""
        return salary > 0

# Instance method - needs object
emp = Employee("Ragul", 50000)
print(emp.get_details())  # Ragul earns ₹50000

# Class method - can call without object
print(f"Company: {Employee.get_company()}")

# Class method as factory
intern = Employee.create_intern("Alice")
print(intern.get_details())  # Alice earns ₹20000

# Static method - utility function
print(f"Is ₹50000 valid? {Employee.is_valid_salary(50000)}")
print(f"Is ₹-100 valid? {Employee.is_valid_salary(-100)}")

# When to use what?
print("\n5️⃣  WHEN TO USE WHAT?")
print("-" * 60)

class Pizza:
    """Example showing all three types"""
    
    base_price = 100  # Class attribute
    
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
    
    # Instance method - works with THIS pizza
    def calculate_price(self):
        """Calculate price for this specific pizza"""
        price = Pizza.base_price
        if self.size == "large":
            price += 50
        price += len(self.toppings) * 20
        return price
    
    # Class method - works with Pizza class
    @classmethod
    def margherita(cls):
        """Factory method - create standard margherita"""
        return cls("medium", ["cheese", "tomato"])
    
    @classmethod
    def update_base_price(cls, new_price):
        """Update price for ALL pizzas"""
        cls.base_price = new_price
    
    # Static method - utility, doesn't need pizza data
    @staticmethod
    def is_valid_size(size):
        """Check if size is valid"""
        return size in ["small", "medium", "large"]

# Instance method
pizza1 = Pizza("large", ["cheese", "pepperoni", "mushroom"])
print(f"Pizza 1 price: ₹{pizza1.calculate_price()}")

# Class method (factory)
pizza2 = Pizza.margherita()
print(f"Margherita price: ₹{pizza2.calculate_price()}")

# Class method (modify class data)
Pizza.update_base_price(120)
print(f"New base price: ₹{Pizza.base_price}")

# Static method (utility)
print(f"Is 'jumbo' valid? {Pizza.is_valid_size('jumbo')}")
print(f"Is 'large' valid? {Pizza.is_valid_size('large')}")

# Summary
print("\n6️⃣  SUMMARY")
print("-" * 60)
print("Instance Method:")
print("  - Uses 'self'")
print("  - Accesses instance data")
print("  - Needs object to call")
print("  - Example: obj.method()")

print("\nClass Method:")
print("  - Uses 'cls'")
print("  - Accesses class data")
print("  - Can call without object")
print("  - Example: Class.method()")
print("  - Use @classmethod decorator")

print("\nStatic Method:")
print("  - No 'self' or 'cls'")
print("  - Utility function")
print("  - Can call without object")
print("  - Example: Class.method()")
print("  - Use @staticmethod decorator")

print()
