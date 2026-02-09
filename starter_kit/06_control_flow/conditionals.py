# ============================================
# IF-ELIF-ELSE STATEMENTS
# ============================================

print("=" * 60)
print("CONDITIONAL STATEMENTS - IF, ELIF, ELSE")
print("=" * 60)

# Simple if
print("\n1️⃣  SIMPLE IF")
print("-" * 60)
age = 20
if age >= 18:
    print(f"Age {age}: You are an adult ✅")

# if-else
print("\n2️⃣  IF-ELSE")
print("-" * 60)
temperature = 25
if temperature > 30:
    print("It's hot! 🔥")
else:
    print("It's pleasant! 😊")

# if-elif-else
print("\n3️⃣  IF-ELIF-ELSE")
print("-" * 60)
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")

# Nested if
print("\n4️⃣  NESTED IF")
print("-" * 60)
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("✅ You can drive!")
    else:
        print("❌ You need a license")
else:
    print("❌ You're too young to drive")

# Multiple conditions (and, or, not)
print("\n5️⃣  MULTIPLE CONDITIONS")
print("-" * 60)
username = "admin"
password = "secret123"

# AND - both must be true
if username == "admin" and password == "secret123":
    print("✅ Login successful!")

# OR - at least one must be true
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("🎉 Day off!")

# NOT - reverse the condition
is_banned = False
if not is_banned:
    print("✅ Account active")

# Ternary operator (one-line if-else)
print("\n6️⃣  TERNARY OPERATOR")
print("-" * 60)
age = 17
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")

# Practical examples
print("\n7️⃣  PRACTICAL EXAMPLES")
print("-" * 60)

# Example 1: Discount calculation
price = 1000
discount = 0.2 if price > 500 else 0.1
final_price = price * (1 - discount)
print(f"Price: ₹{price}, Discount: {discount*100}%, Final: ₹{final_price}")

# Example 2: Grade calculator
marks = 78
if marks >= 90:
    print(f"Marks {marks}: Excellent! 🌟")
elif marks >= 75:
    print(f"Marks {marks}: Very Good! 👍")
elif marks >= 60:
    print(f"Marks {marks}: Good! ✅")
else:
    print(f"Marks {marks}: Need improvement 📚")

# Example 3: Number classification
num = -5
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")

print()
