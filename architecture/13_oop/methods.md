# Instance vs Class vs Static Methods - Simple Guide

## Quick Comparison

| Type         | Uses    | Access        | Call Without Object? | Decorator       |
| ------------ | ------- | ------------- | -------------------- | --------------- |
| **Instance** | `self`  | Instance data | ❌ No                | None            |
| **Class**    | `cls`   | Class data    | ✅ Yes               | `@classmethod`  |
| **Static**   | Neither | Nothing       | ✅ Yes               | `@staticmethod` |

---

## 1. Instance Methods

**Instance methods** work with individual objects (instances).

### Characteristics

- Use `self` parameter
- Access instance attributes (`self.name`)
- Need an object to call
- Most common type

### Example

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

    def bark(self):
        """Instance method - uses self"""
        return f"{self.name} says Woof!"

    def get_age(self):
        """Access instance data"""
        return self.age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Call instance methods
print(dog1.bark())  # Buddy says Woof!
print(dog2.bark())  # Max says Woof!
```

### When to Use

✅ When you need to work with **specific object data**  
✅ When behavior depends on **object state**  
✅ Most methods in a class are instance methods

---

## 2. Class Methods

**Class methods** work with the class itself, not individual objects.

### Characteristics

- Use `cls` parameter (refers to the class)
- Access class attributes
- Can call without creating object
- Use `@classmethod` decorator

### Example

```python
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
        """Modify class attribute"""
        cls.school = new_school

    @classmethod
    def get_count(cls):
        """Access class data"""
        return cls.student_count

# Call without creating object
print(Student.get_school())  # ABC School

# Create students
s1 = Student("Alice")
s2 = Student("Bob")

print(Student.get_count())  # 2

# Change for all students
Student.change_school("XYZ School")
```

### Factory Methods

Class methods are often used as **factory methods** to create objects:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def create_intern(cls, name):
        """Factory method - creates intern with fixed salary"""
        return cls(name, 20000)

    @classmethod
    def create_manager(cls, name):
        """Factory method - creates manager"""
        return cls(name, 100000)

# Use factory methods
intern = Employee.create_intern("Alice")
manager = Employee.create_manager("Bob")

print(intern.salary)   # 20000
print(manager.salary)  # 100000
```

### When to Use

✅ When you need to work with **class-level data**  
✅ For **factory methods** (alternative constructors)  
✅ When you need to **modify class attributes**

---

## 3. Static Methods

**Static methods** are utility functions that belong to the class but don't need access to class or instance data.

### Characteristics

- No `self` or `cls` parameter
- Can't access instance or class data
- Can call without creating object
- Use `@staticmethod` decorator

### Example

```python
class MathUtils:
    """Utility class with static methods"""

    @staticmethod
    def add(a, b):
        """Static method - no self or cls"""
        return a + b

    @staticmethod
    def is_even(num):
        """Utility function"""
        return num % 2 == 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Conversion function"""
        return (celsius * 9/5) + 32

# Call without creating object
print(MathUtils.add(5, 3))                    # 8
print(MathUtils.is_even(10))                  # True
print(MathUtils.celsius_to_fahrenheit(25))    # 77.0
```

### When to Use

✅ For **utility functions** related to the class  
✅ When you don't need **instance or class data**  
✅ For **helper functions** that logically belong to the class

---

## All Three Together

Here's a complete example using all three types:

```python
class Pizza:
    base_price = 100  # Class attribute

    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    # INSTANCE METHOD - works with THIS pizza
    def calculate_price(self):
        """Calculate price for this specific pizza"""
        price = Pizza.base_price
        if self.size == "large":
            price += 50
        price += len(self.toppings) * 20
        return price

    # CLASS METHOD - works with Pizza class
    @classmethod
    def margherita(cls):
        """Factory method - create standard margherita"""
        return cls("medium", ["cheese", "tomato"])

    @classmethod
    def update_base_price(cls, new_price):
        """Update price for ALL pizzas"""
        cls.base_price = new_price

    # STATIC METHOD - utility, doesn't need pizza data
    @staticmethod
    def is_valid_size(size):
        """Check if size is valid"""
        return size in ["small", "medium", "large"]

# Instance method
pizza1 = Pizza("large", ["cheese", "pepperoni"])
print(pizza1.calculate_price())  # 190

# Class method (factory)
pizza2 = Pizza.margherita()
print(pizza2.calculate_price())  # 140

# Class method (modify class data)
Pizza.update_base_price(120)

# Static method (utility)
print(Pizza.is_valid_size("jumbo"))  # False
print(Pizza.is_valid_size("large"))  # True
```

---

## Decision Tree

**Which method type should I use?**

```
Do you need instance data (self.attribute)?
├─ YES → Use INSTANCE METHOD
└─ NO
   │
   Do you need class data (cls.attribute)?
   ├─ YES → Use CLASS METHOD
   └─ NO → Use STATIC METHOD
```

---

## Common Patterns

### Pattern 1: Instance Method (Most Common)

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        """Needs instance data"""
        self.balance += amount
```

### Pattern 2: Class Method (Factory)

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        """Create Date for today"""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)

date = Date.today()
```

### Pattern 3: Static Method (Utility)

```python
class StringUtils:
    @staticmethod
    def reverse(text):
        """Utility function"""
        return text[::-1]

result = StringUtils.reverse("hello")
```

---

## Summary

| Method Type  | Purpose                         | Example Use Case                  |
| ------------ | ------------------------------- | --------------------------------- |
| **Instance** | Work with object data           | `account.deposit(100)`            |
| **Class**    | Work with class data or factory | `Employee.create_intern("Alice")` |
| **Static**   | Utility functions               | `MathUtils.add(5, 3)`             |

**Remember:**

- **Instance methods** = Most common, work with object
- **Class methods** = Work with class, good for factories
- **Static methods** = Utilities, no access to class/instance data

📁 [methods-comparison.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/oop/methods-comparison.py)
