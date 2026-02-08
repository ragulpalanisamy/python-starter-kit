# ============================================
# INHERITANCE
# ============================================

print("=" * 60)
print("INHERITANCE - Reusing Code")
print("=" * 60)

# Basic inheritance
print("\n1️⃣  BASIC INHERITANCE")
print("-" * 60)

class Animal:
    """Parent class (Base class)"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """Generic speak method"""
        print(f"{self.name} makes a sound")

class Dog(Animal):
    """Child class (Derived class)"""
    
    def speak(self):
        """Override parent method"""
        print(f"{self.name} barks: Woof!")

class Cat(Animal):
    """Another child class"""
    
    def speak(self):
        """Override parent method"""
        print(f"{self.name} meows: Meow!")

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()

# Calling parent methods
print("\n2️⃣  CALLING PARENT METHODS (super())")
print("-" * 60)

class Vehicle:
    """Parent class"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        print(f"Vehicle: {self.brand} {self.model}")

class Car(Vehicle):
    """Child class"""
    
    def __init__(self, brand, model, doors):
        # Call parent constructor
        super().__init__(brand, model)
        self.doors = doors
    
    def info(self):
        """Override and extend parent method"""
        super().info()  # Call parent method
        print(f"Doors: {self.doors}")

car = Car("Toyota", "Camry", 4)
car.info()

# Multiple inheritance
print("\n3️⃣  MULTIPLE INHERITANCE")
print("-" * 60)

class Flyable:
    """Mixin class for flying"""
    
    def fly(self):
        print("Flying in the sky!")

class Swimmable:
    """Mixin class for swimming"""
    
    def swim(self):
        print("Swimming in water!")

class Duck(Animal, Flyable, Swimmable):
    """Duck can do everything"""
    
    def speak(self):
        print(f"{self.name} quacks: Quack!")

duck = Duck("Donald")
duck.speak()
duck.fly()
duck.swim()

# Inheritance hierarchy
print("\n4️⃣  INHERITANCE HIERARCHY")
print("-" * 60)

class Employee:
    """Base employee class"""
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"Employee: {self.name}, Salary: ₹{self.salary}")

class Manager(Employee):
    """Manager inherits from Employee"""
    
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def display(self):
        super().display()
        print(f"Team size: {self.team_size}")

class Developer(Employee):
    """Developer inherits from Employee"""
    
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    def display(self):
        super().display()
        print(f"Language: {self.language}")

manager = Manager("Alice", 100000, 5)
developer = Developer("Bob", 80000, "Python")

print("Manager:")
manager.display()

print("\nDeveloper:")
developer.display()

# Checking inheritance
print("\n5️⃣  CHECKING INHERITANCE")
print("-" * 60)

print(f"Is dog an Animal? {isinstance(dog, Animal)}")
print(f"Is dog a Dog? {isinstance(dog, Dog)}")
print(f"Is dog a Cat? {isinstance(dog, Cat)}")

print(f"\nIs Dog subclass of Animal? {issubclass(Dog, Animal)}")
print(f"Is Cat subclass of Animal? {issubclass(Cat, Animal)}")
print(f"Is Dog subclass of Cat? {issubclass(Dog, Cat)}")

print()
