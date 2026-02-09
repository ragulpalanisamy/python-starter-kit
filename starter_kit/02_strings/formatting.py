# ============================================
# STRING FORMATTING
# ============================================

print("=" * 60)
print("STRING FORMATTING")
print("=" * 60)

name = "Ragul"
age = 25
price = 99.99

# Method 1: f-strings (Python 3.6+) - RECOMMENDED
print("\n1️⃣  F-STRINGS (Recommended)")
print("-" * 60)
print(f"Hello, {name}!")
print(f"{name} is {age} years old")
print(f"Price: ₹{price:.2f}")
print(f"Expression: 10 + 5 = {10 + 5}")

# Method 2: format() method
print("\n2️⃣  FORMAT() METHOD")
print("-" * 60)
print("Hello, {}!".format(name))
print("{} is {} years old".format(name, age))
print("Price: ₹{:.2f}".format(price))
print("{1} is {0} years old".format(age, name))  # Positional
print("{n} is {a} years old".format(n=name, a=age))  # Named

# Method 3: % formatting (old style)
print("\n3️⃣  % FORMATTING (Old Style)")
print("-" * 60)
print("Hello, %s!" % name)
print("%s is %d years old" % (name, age))
print("Price: ₹%.2f" % price)

# Advanced f-string formatting
print("\n4️⃣  ADVANCED F-STRING FORMATTING")
print("-" * 60)

# Alignment
text = "Python"
print(f"Left align: '{text:<10}'")
print(f"Right align: '{text:>10}'")
print(f"Center: '{text:^10}'")

# Number formatting
num = 1234567.89
print(f"Comma separator: {num:,}")
print(f"2 decimals: {num:.2f}")
print(f"Percentage: {0.85:.1%}")

# Padding with zeros
number = 42
print(f"Zero padding: {number:05d}")

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"Date: {now:%Y-%m-%d}")
print(f"Time: {now:%H:%M:%S}")

print()
