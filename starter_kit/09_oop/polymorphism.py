# ============================================
# POLYMORPHISM
# ============================================

print("=" * 60)
print("POLYMORPHISM - Many Forms")
print("=" * 60)

# Method overriding
print("\n1️⃣  METHOD OVERRIDING")
print("-" * 60)

class Shape:
    """Base shape class"""
    
    def area(self):
        """Calculate area"""
        return 0

class Rectangle(Shape):
    """Rectangle class"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Override area method"""
        return self.width * self.height

class Circle(Shape):
    """Circle class"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Override area method"""
        return 3.14159 * self.radius ** 2

# Same method name, different behavior
rectangle = Rectangle(10, 5)
circle = Circle(7)

print(f"Rectangle area: {rectangle.area()}")
print(f"Circle area: {circle.area():.2f}")

# Polymorphism with functions
print("\n2️⃣  POLYMORPHISM WITH FUNCTIONS")
print("-" * 60)

def print_area(shape):
    """Function that works with any shape"""
    print(f"Area: {shape.area():.2f}")

# Same function, different objects
print("Rectangle:")
print_area(rectangle)

print("Circle:")
print_area(circle)

# Duck typing
print("\n3️⃣  DUCK TYPING")
print("-" * 60)
print("If it walks like a duck and quacks like a duck, it's a duck!")

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

def animal_sound(animal):
    """Works with any object that has speak() method"""
    print(animal.speak())

dog = Dog()
cat = Cat()
duck = Duck()

animal_sound(dog)
animal_sound(cat)
animal_sound(duck)

# Operator overloading
print("\n4️⃣  OPERATOR OVERLOADING")
print("-" * 60)

class Point:
    """Point class with operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        """Overload + operator"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload - operator"""
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y

p1 = Point(10, 20)
p2 = Point(5, 10)

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 + p2: {p1 + p2}")
print(f"p1 - p2: {p1 - p2}")
print(f"p1 == p2: {p1 == p2}")

# Method overloading (using default arguments)
print("\n5️⃣  METHOD OVERLOADING (Default Arguments)")
print("-" * 60)

class Calculator:
    """Calculator with flexible methods"""
    
    def add(self, a, b=0, c=0):
        """Add 1, 2, or 3 numbers"""
        return a + b + c

calc = Calculator()
print(f"add(5): {calc.add(5)}")
print(f"add(5, 3): {calc.add(5, 3)}")
print(f"add(5, 3, 2): {calc.add(5, 3, 2)}")

# Polymorphism with collections
print("\n6️⃣  POLYMORPHISM WITH COLLECTIONS")
print("-" * 60)

shapes = [
    Rectangle(10, 5),
    Circle(7),
    Rectangle(8, 4),
    Circle(3)
]

print("Calculating areas:")
total_area = 0
for shape in shapes:
    area = shape.area()
    print(f"  {shape.__class__.__name__}: {area:.2f}")
    total_area += area

print(f"Total area: {total_area:.2f}")

print()
