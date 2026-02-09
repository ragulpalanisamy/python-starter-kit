# ============================================
# ABSTRACTION
# ============================================

print("=" * 60)
print("ABSTRACTION - Hiding Complexity")
print("=" * 60)

from abc import ABC, abstractmethod

# Abstract base class
print("\n1️⃣  ABSTRACT BASE CLASS")
print("-" * 60)

class Animal(ABC):
    """Abstract animal class"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        """Abstract method - must be implemented by child classes"""
        pass
    
    @abstractmethod
    def move(self):
        """Abstract method"""
        pass

class Dog(Animal):
    """Concrete dog class"""
    
    def speak(self):
        return f"{self.name} barks: Woof!"
    
    def move(self):
        return f"{self.name} runs on four legs"

class Bird(Animal):
    """Concrete bird class"""
    
    def speak(self):
        return f"{self.name} chirps: Tweet!"
    
    def move(self):
        return f"{self.name} flies in the sky"

# Cannot create instance of abstract class
# animal = Animal("Generic")  # ❌ Error!

# Can create instances of concrete classes
dog = Dog("Buddy")
bird = Bird("Tweety")

print(dog.speak())
print(dog.move())
print(bird.speak())
print(bird.move())

# Abstract class with concrete methods
print("\n2️⃣  ABSTRACT CLASS WITH CONCRETE METHODS")
print("-" * 60)

class Vehicle(ABC):
    """Abstract vehicle class"""
    
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def start(self):
        """Abstract method"""
        pass
    
    def stop(self):
        """Concrete method - shared by all vehicles"""
        return f"{self.brand} stopped"

class Car(Vehicle):
    """Concrete car class"""
    
    def start(self):
        return f"{self.brand} car engine started"

class Bike(Vehicle):
    """Concrete bike class"""
    
    def start(self):
        return f"{self.brand} bike engine started"

car = Car("Toyota")
bike = Bike("Honda")

print(car.start())
print(car.stop())
print(bike.start())
print(bike.stop())

# Interface-like abstract class
print("\n3️⃣  INTERFACE-LIKE ABSTRACT CLASS")
print("-" * 60)

class PaymentProcessor(ABC):
    """Payment processor interface"""
    
    @abstractmethod
    def process_payment(self, amount):
        """Process payment"""
        pass
    
    @abstractmethod
    def refund(self, amount):
        """Process refund"""
        pass

class CreditCardProcessor(PaymentProcessor):
    """Credit card payment processor"""
    
    def process_payment(self, amount):
        return f"Processing ₹{amount} via Credit Card"
    
    def refund(self, amount):
        return f"Refunding ₹{amount} to Credit Card"

class UPIProcessor(PaymentProcessor):
    """UPI payment processor"""
    
    def process_payment(self, amount):
        return f"Processing ₹{amount} via UPI"
    
    def refund(self, amount):
        return f"Refunding ₹{amount} to UPI"

def make_payment(processor, amount):
    """Function that works with any payment processor"""
    print(processor.process_payment(amount))

cc = CreditCardProcessor()
upi = UPIProcessor()

make_payment(cc, 1000)
make_payment(upi, 500)

# Real-world example: Database abstraction
print("\n4️⃣  REAL-WORLD EXAMPLE: DATABASE")
print("-" * 60)

class Database(ABC):
    """Abstract database class"""
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute(self, query):
        pass
    
    @abstractmethod
    def close(self):
        pass

class MySQLDatabase(Database):
    """MySQL implementation"""
    
    def connect(self):
        return "Connected to MySQL"
    
    def execute(self, query):
        return f"Executing in MySQL: {query}"
    
    def close(self):
        return "MySQL connection closed"

class PostgreSQLDatabase(Database):
    """PostgreSQL implementation"""
    
    def connect(self):
        return "Connected to PostgreSQL"
    
    def execute(self, query):
        return f"Executing in PostgreSQL: {query}"
    
    def close(self):
        return "PostgreSQL connection closed"

def run_query(db, query):
    """Run query on any database"""
    print(db.connect())
    print(db.execute(query))
    print(db.close())

mysql = MySQLDatabase()
postgres = PostgreSQLDatabase()

print("MySQL:")
run_query(mysql, "SELECT * FROM users")

print("\nPostgreSQL:")
run_query(postgres, "SELECT * FROM users")

print()
