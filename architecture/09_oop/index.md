# Python OOP - Simple & Easy Guide

## Table of Contents

1. [What is OOP?](#what-is-oop)
2. [Classes and Objects](#classes-objects)
3. [The 4 Pillars of OOP](#four-pillars)
4. [Practical Examples](#practical)

---

## What is OOP? {#what-is-oop}

**OOP (Object-Oriented Programming)** is a way to organize code using **objects**.

### Real-World Analogy

Think of a **Car**:

- **Properties**: color, brand, speed (data)
- **Actions**: start, stop, accelerate (functions)

In OOP:

- **Class** = Blueprint (like a car design)
- **Object** = Actual thing (like your actual car)
- **Attributes** = Properties (color, brand)
- **Methods** = Actions (start, stop)

### Why Use OOP?

✅ **Organized** - Code is grouped logically  
✅ **Reusable** - Write once, use many times  
✅ **Easy to maintain** - Changes in one place  
✅ **Real-world modeling** - Code matches real objects

---

## Classes and Objects {#classes-objects}

### Creating a Class

A **class** is a blueprint for creating objects.

```python
class Dog:
    """A simple dog class"""
    pass

# Create object (instance)
my_dog = Dog()
```

### Adding Attributes (Properties)

Attributes store data about the object.

```python
class Dog:
    def __init__(self, name, age):
        """Constructor - runs when creating object"""
        self.name = name  # Attribute
        self.age = age    # Attribute

# Create dogs with different data
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # Buddy
print(dog2.age)   # 5
```

**Key Points:**

- `__init__` is the **constructor** (optional, but common)
- `self` refers to the **current object**
- `self.name` creates an **attribute**

### Adding Methods (Actions)

Methods are functions that belong to a class.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        """Method - action the dog can do"""
        print(f"{self.name} says Woof!")

    def eat(self, food):
        """Method with parameter"""
        print(f"{self.name} is eating {food}")

dog = Dog("Buddy")
dog.bark()           # Buddy says Woof!
dog.eat("bones")     # Buddy is eating bones
```

### Complete Example: Bank Account

```python
class BankAccount:
    """Simple bank account"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money"""
        self.balance += amount
        print(f"Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        """Take money"""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Balance: ₹{self.balance}")
        else:
            print("Not enough money!")

    def check_balance(self):
        """See balance"""
        return self.balance

# Create account
account = BankAccount("Ragul", 1000)
account.deposit(500)    # Deposited ₹500. Balance: ₹1500
account.withdraw(200)   # Withdrew ₹200. Balance: ₹1300
print(account.check_balance())  # 1300
```

📁 [class-basics.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/oop/class-basics.py)

---

## The 4 Pillars of OOP {#four-pillars}

### 1. Inheritance - Reusing Code 👨‍👦

**Inheritance** = Child class gets everything from parent class.

**Real-world analogy:** You inherit traits from your parents.

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks: Woof!")

# Child class (inherits from Animal)
class Cat(Animal):
    def meow(self):
        print(f"{self.name} meows: Meow!")

# Both Dog and Cat have sleep() from Animal
dog = Dog("Buddy")
dog.sleep()  # Buddy is sleeping (inherited)
dog.bark()   # Buddy barks: Woof! (own method)

cat = Cat("Whiskers")
cat.sleep()  # Whiskers is sleeping (inherited)
cat.meow()   # Whiskers meows: Meow! (own method)
```

**Why useful?**

- ✅ Don't repeat code
- ✅ Easy to add new types
- ✅ Changes in parent affect all children

**Using `super()` to call parent:**

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)  # Call parent constructor
        self.doors = doors

car = Car("Toyota", 4)
print(car.brand)  # Toyota (from parent)
print(car.doors)  # 4 (own attribute)
```

📁 [inheritance.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/oop/inheritance.py)

---

### 2. Encapsulation - Hiding Data 🔒

**Encapsulation** = Hide internal details, show only what's needed.

**Real-world analogy:** ATM machine - you use buttons, but don't see internal wiring.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private (hidden)

    def deposit(self, amount):
        """Public method to add money"""
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        """Public method to see balance"""
        return self.__balance

account = BankAccount(1000)
# account.__balance = 999999  # ❌ Can't access directly
account.deposit(500)           # ✅ Use public method
print(account.get_balance())   # ✅ Use public method
```

**Access Levels:**

| Type          | Syntax        | Meaning                   |
| ------------- | ------------- | ------------------------- |
| **Public**    | `self.name`   | Anyone can access         |
| **Protected** | `self._name`  | Internal use (convention) |
| **Private**   | `self.__name` | Hidden from outside       |

**Using `@property` (Pythonic way):**

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        """Getter - read age"""
        return self._age

    @age.setter
    def age(self, value):
        """Setter - set age with validation"""
        if 0 < value < 120:
            self._age = value
        else:
            print("Invalid age!")

person = Person(25)
print(person.age)  # 25 (uses getter)
person.age = 30    # Uses setter
person.age = 150   # Invalid age!
```

**Why useful?**

- ✅ Protect data from invalid changes
- ✅ Control how data is accessed
- ✅ Can change internal code without breaking external code

📁 [encapsulation.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/oop/encapsulation.py)

---

### 3. Polymorphism - Many Forms 🎭

**Polymorphism** = Same action, different behavior.

**Real-world analogy:** "Draw" means different things - draw a circle, draw a square.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"

# Same method name, different behavior
def make_sound(animal):
    """Works with any animal"""
    print(animal.speak())

dog = Dog()
cat = Cat()
cow = Cow()

make_sound(dog)  # Woof!
make_sound(cat)  # Meow!
make_sound(cow)  # Moo!
```

**Method Overriding:**

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Override parent method"""
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Override parent method"""
        return 3.14 * self.radius ** 2

# Same method name, different calculation
rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())    # 50
print(circle.area())  # 153.86
```

**Operator Overloading:**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Define what + means for Point"""
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses __add__
print(p3)     # (4, 6)
```

**Why useful?**

- ✅ Same interface for different objects
- ✅ Flexible and extensible code
- ✅ Easy to add new types

📁 [polymorphism.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/oop/polymorphism.py)

---

### 4. Abstraction - Hiding Complexity 🎨

**Abstraction** = Show only essential features, hide complex details.

**Real-world analogy:** Driving a car - you use steering wheel, not worrying about engine internals.

```python
from abc import ABC, abstractmethod

# Abstract class (blueprint)
class Animal(ABC):
    """Cannot create Animal directly"""

    @abstractmethod
    def speak(self):
        """Every animal MUST implement speak"""
        pass

    @abstractmethod
    def move(self):
        """Every animal MUST implement move"""
        pass

# Concrete class (actual implementation)
class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "Running on 4 legs"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

    def move(self):
        return "Flying"

# animal = Animal()  # ❌ Error! Can't create abstract class
dog = Dog()          # ✅ OK
bird = Bird()        # ✅ OK

print(dog.speak())   # Woof!
print(bird.move())   # Flying
```

**Real-world example: Payment System**

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    """Abstract payment interface"""

    @abstractmethod
    def pay(self, amount):
        """All payment methods must implement pay"""
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Paid ₹{amount} via Credit Card"

class UPI(PaymentMethod):
    def pay(self, amount):
        return f"Paid ₹{amount} via UPI"

class Cash(PaymentMethod):
    def pay(self, amount):
        return f"Paid ₹{amount} in Cash"

def process_payment(payment_method, amount):
    """Works with any payment method"""
    print(payment_method.pay(amount))

# All use same interface
process_payment(CreditCard(), 1000)  # Paid ₹1000 via Credit Card
process_payment(UPI(), 500)          # Paid ₹500 via UPI
process_payment(Cash(), 200)         # Paid ₹200 in Cash
```

**Why useful?**

- ✅ Forces consistent interface
- ✅ Hides complex implementation
- ✅ Easy to swap implementations

📁 [abstraction.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/oop/abstraction.py)

---

## Practical Examples {#practical}

### Example 1: Library System

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Borrowed: {self.title}")
        else:
            print(f"{self.title} is already borrowed")

    def return_book(self):
        self.is_borrowed = False
        print(f"Returned: {self.title}")

# Create books
book1 = Book("Python Basics", "John Doe")
book2 = Book("Data Science", "Jane Smith")

# Use books
book1.borrow()   # Borrowed: Python Basics
book1.borrow()   # Python Basics is already borrowed
book1.return_book()  # Returned: Python Basics
```

### Example 2: Shopping Cart

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product, quantity=1):
        self.items.append({"product": product, "qty": quantity})
        print(f"Added {quantity}x {product.name}")

    def total(self):
        return sum(item["product"].price * item["qty"]
                   for item in self.items)

    def show(self):
        print("\n🛒 Cart:")
        for item in self.items:
            p = item["product"]
            q = item["qty"]
            print(f"  {p.name} x{q} = ₹{p.price * q}")
        print(f"  Total: ₹{self.total()}")

# Shopping
cart = Cart()
cart.add(Product("Laptop", 50000), 1)
cart.add(Product("Mouse", 500), 2)
cart.show()
```

### Example 3: Student Grades

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, marks):
        self.grades[subject] = marks

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def report(self):
        print(f"\n📊 {self.name}'s Report:")
        for subject, marks in self.grades.items():
            print(f"  {subject}: {marks}")
        print(f"  Average: {self.average():.1f}")

# Create student
student = Student("Ragul")
student.add_grade("Math", 85)
student.add_grade("Science", 92)
student.add_grade("English", 78)
student.report()
```

📁 [practical.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/oop/practical.py)

---

## Quick Summary

### Basic Concepts

| Term            | Simple Explanation              | Example               |
| --------------- | ------------------------------- | --------------------- |
| **Class**       | Blueprint/Template              | `class Dog:`          |
| **Object**      | Actual thing created from class | `my_dog = Dog()`      |
| **Attribute**   | Data/Property                   | `self.name = "Buddy"` |
| **Method**      | Action/Function                 | `def bark(self):`     |
| **Constructor** | Setup when creating object      | `def __init__(self):` |
| **self**        | Refers to current object        | `self.name`           |

### The 4 Pillars

| Pillar            | Simple Meaning               | Real-World Example               |
| ----------------- | ---------------------------- | -------------------------------- |
| **Inheritance**   | Child gets parent's features | You inherit from parents         |
| **Encapsulation** | Hide internal details        | ATM hides internal wiring        |
| **Polymorphism**  | Same action, different forms | "Draw" circle vs square          |
| **Abstraction**   | Hide complexity              | Drive car without knowing engine |

### When to Use What

**Use Inheritance when:**

- ✅ You have "is-a" relationship (Dog **is an** Animal)
- ✅ You want to reuse code
- ✅ You want to extend existing functionality

**Use Encapsulation when:**

- ✅ You want to protect data
- ✅ You want to control access
- ✅ You want to validate input

**Use Polymorphism when:**

- ✅ Different objects need same interface
- ✅ You want flexible, extensible code
- ✅ You want to treat different types uniformly

**Use Abstraction when:**

- ✅ You want to define a contract/interface
- ✅ You want to hide implementation details
- ✅ You want to force consistent behavior

---

## Common Patterns

### Pattern 1: Simple Data Container

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Ragul", 25)
```

### Pattern 2: Utility Class (No Constructor)

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(5, 3)
```

### Pattern 3: Inheritance Hierarchy

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
```

---

## Remember

✅ **Classes** are blueprints, **objects** are actual things  
✅ **Attributes** store data, **methods** perform actions  
✅ **Constructor** (`__init__`) is optional but common  
✅ **self** always refers to the current object  
✅ **Inheritance** = reuse code  
✅ **Encapsulation** = hide data  
✅ **Polymorphism** = many forms  
✅ **Abstraction** = hide complexity

**Start simple, add complexity as needed!** 🚀
