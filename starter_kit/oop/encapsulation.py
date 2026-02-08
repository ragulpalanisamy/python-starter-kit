# ============================================
# ENCAPSULATION
# ============================================

print("=" * 60)
print("ENCAPSULATION - Data Hiding")
print("=" * 60)

# Public, Protected, Private attributes
print("\n1️⃣  PUBLIC, PROTECTED, PRIVATE")
print("-" * 60)

class BankAccount:
    """Bank account with encapsulation"""
    
    def __init__(self, owner, balance):
        self.owner = owner           # Public
        self._account_number = "123" # Protected (convention)
        self.__balance = balance     # Private (name mangling)
    
    def get_balance(self):
        """Public method to access private attribute"""
        return self.__balance
    
    def deposit(self, amount):
        """Public method to modify private attribute"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid amount!")
    
    def __validate_pin(self, pin):
        """Private method"""
        return pin == "1234"

account = BankAccount("Ragul", 1000)

# Public attribute - accessible
print(f"Owner: {account.owner}")

# Protected attribute - accessible but shouldn't be used
print(f"Account number: {account._account_number}")

# Private attribute - not directly accessible
# print(account.__balance)  # ❌ Error!
print(f"Balance (via getter): {account.get_balance()}")

account.deposit(500)
print(f"New balance: {account.get_balance()}")

# Property decorator (Pythonic way)
print("\n2️⃣  PROPERTY DECORATOR (@property)")
print("-" * 60)

class Temperature:
    """Temperature class with property"""
    
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")

# Set temperature
temp.celsius = 30
print(f"New Celsius: {temp.celsius}°C")
print(f"New Fahrenheit: {temp.fahrenheit}°F")

# Getters and Setters
print("\n3️⃣  GETTERS AND SETTERS")
print("-" * 60)

class Person:
    """Person class with getters and setters"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    # Getter
    def get_name(self):
        return self._name
    
    # Setter
    def set_name(self, name):
        if name:
            self._name = name
        else:
            print("Name cannot be empty!")
    
    # Getter
    def get_age(self):
        return self._age
    
    # Setter with validation
    def set_age(self, age):
        if 0 < age < 120:
            self._age = age
        else:
            print("Invalid age!")

person = Person("Ragul", 25)
print(f"Name: {person.get_name()}")
print(f"Age: {person.get_age()}")

person.set_age(26)
print(f"New age: {person.get_age()}")

person.set_age(150)  # Invalid

# Read-only property
print("\n4️⃣  READ-ONLY PROPERTY")
print("-" * 60)

class Circle:
    """Circle with read-only area"""
    
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive!")
    
    @property
    def area(self):
        """Read-only computed property"""
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area:.2f}")

circle.radius = 10
print(f"New radius: {circle.radius}")
print(f"New area: {circle.area:.2f}")

# circle.area = 100  # ❌ Error: can't set attribute

print()
