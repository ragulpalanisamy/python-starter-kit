# ============================================
# PRACTICAL OOP EXAMPLES
# ============================================

print("=" * 60)
print("PRACTICAL OOP EXAMPLES")
print("=" * 60)

# Example 1: Library Management System
print("\n1️⃣  LIBRARY MANAGEMENT SYSTEM")
print("-" * 60)

class Book:
    """Book class"""
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def return_book(self):
        self.is_borrowed = False
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"

class Library:
    """Library class"""
    
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")
    
    def display_books(self):
        print(f"\n{self.name} - Books:")
        for book in self.books:
            print(f"  {book}")

# Create library
library = Library("City Library")

# Add books
library.add_book(Book("Python Basics", "John Doe", "123"))
library.add_book(Book("Data Science", "Jane Smith", "456"))

# Display books
library.display_books()

# Borrow book
library.books[0].borrow()
library.display_books()

# Example 2: E-commerce System
print("\n2️⃣  E-COMMERCE SYSTEM")
print("-" * 60)

class Product:
    """Product class"""
    
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def __str__(self):
        return f"{self.name} - ₹{self.price} ({self.stock} in stock)"

class ShoppingCart:
    """Shopping cart class"""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, product, quantity=1):
        if product.stock >= quantity:
            self.items.append({"product": product, "quantity": quantity})
            product.stock -= quantity
            print(f"Added {quantity}x {product.name}")
        else:
            print(f"Not enough stock for {product.name}")
    
    def get_total(self):
        return sum(item["product"].price * item["quantity"] for item in self.items)
    
    def display(self):
        print("\nShopping Cart:")
        for item in self.items:
            p = item["product"]
            q = item["quantity"]
            print(f"  {p.name} x{q} = ₹{p.price * q}")
        print(f"Total: ₹{self.get_total()}")

# Create products
laptop = Product("Laptop", 50000, 5)
mouse = Product("Mouse", 500, 20)

# Create cart and add items
cart = ShoppingCart()
cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
cart.display()

# Example 3: Student Management System
print("\n3️⃣  STUDENT MANAGEMENT SYSTEM")
print("-" * 60)

class Student:
    """Student class"""
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.grades = {}
    
    def add_grade(self, subject, marks):
        self.grades[subject] = marks
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    
    def display(self):
        print(f"\nStudent: {self.name} (Roll No: {self.roll_no})")
        print("Grades:")
        for subject, marks in self.grades.items():
            print(f"  {subject}: {marks}")
        print(f"Average: {self.get_average():.2f}")

# Create student
student = Student("Ragul", "101")
student.add_grade("Math", 85)
student.add_grade("Science", 92)
student.add_grade("English", 78)
student.display()

# Example 4: Banking System
print("\n4️⃣  BANKING SYSTEM")
print("-" * 60)

class Account:
    """Base account class"""
    
    def __init__(self, account_no, holder, balance=0):
        self.account_no = account_no
        self.holder = holder
        self._balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        self._balance += amount
        self.transactions.append(f"Deposited: ₹{amount}")
        return self._balance
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self.transactions.append(f"Withdrew: ₹{amount}")
            return self._balance
        return None
    
    def get_balance(self):
        return self._balance

class SavingsAccount(Account):
    """Savings account with interest"""
    
    def __init__(self, account_no, holder, balance=0, interest_rate=0.04):
        super().__init__(account_no, holder, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        self.transactions.append(f"Interest added: ₹{interest:.2f}")

# Create account
account = SavingsAccount("SA001", "Ragul", 10000)
print(f"Initial balance: ₹{account.get_balance()}")

account.deposit(5000)
print(f"After deposit: ₹{account.get_balance()}")

account.withdraw(2000)
print(f"After withdrawal: ₹{account.get_balance()}")

account.add_interest()
print(f"After interest: ₹{account.get_balance()}")

# Example 5: Game Character System
print("\n5️⃣  GAME CHARACTER SYSTEM")
print("-" * 60)

class Character:
    """Base character class"""
    
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
    
    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    """Warrior class with special ability"""
    
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=25)
    
    def special_attack(self, target):
        damage = self.attack_power * 2
        target.health -= damage
        print(f"{self.name} uses POWER STRIKE on {target.name} for {damage} damage!")

class Mage(Character):
    """Mage class with magic"""
    
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30)
        self.mana = 100
    
    def cast_spell(self, target):
        if self.mana >= 20:
            damage = self.attack_power * 1.5
            target.health -= damage
            self.mana -= 20
            print(f"{self.name} casts FIREBALL on {target.name} for {damage} damage!")
        else:
            print(f"{self.name} doesn't have enough mana!")

# Create characters
warrior = Warrior("Conan")
mage = Mage("Gandalf")

print(f"{warrior.name}: HP={warrior.health}, ATK={warrior.attack_power}")
print(f"{mage.name}: HP={mage.health}, ATK={mage.attack_power}, MANA={mage.mana}")

# Battle
warrior.attack(mage)
print(f"{mage.name} HP: {mage.health}")

mage.cast_spell(warrior)
print(f"{warrior.name} HP: {warrior.health}")

warrior.special_attack(mage)
print(f"{mage.name} HP: {mage.health}")

print()
