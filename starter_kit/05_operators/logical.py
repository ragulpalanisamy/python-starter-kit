# ============================================
# LOGICAL OPERATORS
# ============================================

print("=" * 50)
print("LOGICAL OPERATORS")
print("=" * 50)

a = True
b = False

print(f"\na = {a}, b = {b}\n")

# AND - Returns True if both are True
result = a and b
print(f"{a} and {b} → {result}")

result = True and True
print(f"True and True → {result}")

# OR - Returns True if at least one is True
result = a or b
print(f"{a} or {b} → {result}")

result = False or False
print(f"False or False → {result}")

# NOT - Reverses the boolean value
result = not a
print(f"not {a} → {result}")

result = not b
print(f"not {b} → {result}")

print()

# Practical Examples
print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Login validation
username = "ragul"
password = "secret123"

if username == "ragul" and password == "secret123":
    print("\n✅ Login successful!")
else:
    print("\n❌ Invalid credentials")

# Age and license check for driving
age = 20
has_license = True

if age >= 18 and has_license:
    print(f"\nAge {age} with license: You can drive! 🚗")
else:
    print(f"\nAge {age}: Cannot drive")

# Weekend or holiday check
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("\n🎉 It's a day off! Enjoy!")
else:
    print("\n💼 It's a working day")

# Account status check
is_active = True
is_banned = False

if is_active and not is_banned:
    print("\n✅ Account is active and in good standing")
else:
    print("\n❌ Account has issues")

# Discount eligibility
is_student = True
is_senior = False
age = 22

if is_student or is_senior or age < 12:
    print(f"\n🎫 Eligible for discount!")
else:
    print(f"\n💰 Regular price applies")

print()
