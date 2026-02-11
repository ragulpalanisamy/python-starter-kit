# ============================================
# RAISING EXCEPTIONS
# ============================================

print("=" * 60)
print("RAISING EXCEPTIONS")
print("=" * 60)

# Raising exceptions
print("\n1️⃣  RAISING EXCEPTIONS")
print("-" * 60)

def check_age(age):
    """Check if age is valid"""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 120:
        raise ValueError("Age too high!")
    return True

try:
    check_age(-5)
except ValueError as e:
    print(f"❌ Error: {e}")

try:
    check_age(150)
except ValueError as e:
    print(f"❌ Error: {e}")

print(f"✅ Age 25 is valid: {check_age(25)}")

# Custom exceptions
print("\n2️⃣  CUSTOM EXCEPTIONS")
print("-" * 60)

class InsufficientFundsError(Exception):
    """Custom exception for banking"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ₹{amount}. Balance: ₹{self.balance}"
            )
        self.balance -= amount
        return self.balance

account = BankAccount(1000)

try:
    account.withdraw(500)
    print("✅ Withdrew ₹500")
    account.withdraw(800)  # This will fail
except InsufficientFundsError as e:
    print(f"❌ {e}")

# Re-raising exceptions
print("\n3️⃣  RE-RAISING EXCEPTIONS")
print("-" * 60)

def process_data(data):
    try:
        result = int(data)
        return result
    except ValueError:
        print("⚠️  Logging error...")
        raise  # Re-raise the same exception

try:
    process_data("abc")
except ValueError:
    print("❌ Invalid data!")

# Exception chaining
print("\n4️⃣  EXCEPTION CHAINING")
print("-" * 60)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Division failed") from e

try:
    divide(10, 0)
except ValueError as e:
    print(f"❌ Error: {e}")
    print(f"   Caused by: {e.__cause__}")

# Assert statements
print("\n5️⃣  ASSERT STATEMENTS")
print("-" * 60)

def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty!"
    return sum(numbers) / len(numbers)

try:
    avg = calculate_average([10, 20, 30])
    print(f"✅ Average: {avg}")
    
    avg = calculate_average([])  # This will fail
except AssertionError as e:
    print(f"❌ Assertion failed: {e}")

print()
