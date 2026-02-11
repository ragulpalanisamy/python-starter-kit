# ============================================
# EXCEPTION HANDLING BASICS
# ============================================

print("=" * 60)
print("EXCEPTION HANDLING BASICS")
print("=" * 60)

# What is an exception?
print("\n1️⃣  WHAT IS AN EXCEPTION?")
print("-" * 60)
print("Exception = Error that occurs during program execution")

# Without exception handling (program crashes)
print("\n❌ WITHOUT EXCEPTION HANDLING:")
try:
    # This would crash the program
    # result = 10 / 0  # ZeroDivisionError
    print("Program would crash here!")
except:
    pass

# Basic try-except
print("\n2️⃣  BASIC TRY-EXCEPT")
print("-" * 60)

try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero!")
    result = None

print("Program continues running...")

# Multiple exceptions
print("\n3️⃣  HANDLING MULTIPLE EXCEPTIONS")
print("-" * 60)

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
        return None
    except TypeError:
        print("❌ Invalid type! Use numbers only.")
        return None

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")
print(f"10 / 'a' = {divide(10, 'a')}")

# Catching multiple exceptions together
print("\n4️⃣  CATCHING MULTIPLE EXCEPTIONS TOGETHER")
print("-" * 60)

def safe_divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        print(f"❌ Error: {e}")
        return None

print(f"Result: {safe_divide(10, 0)}")
print(f"Result: {safe_divide(10, 'a')}")

# try-except-else
print("\n5️⃣  TRY-EXCEPT-ELSE")
print("-" * 60)
print("else block runs if NO exception occurs")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("❌ Division by zero!")
else:
    print(f"✅ Success! Result = {result}")

# try-except-finally
print("\n6️⃣  TRY-EXCEPT-FINALLY")
print("-" * 60)
print("finally block ALWAYS runs (cleanup code)")

try:
    file = open("test.txt", "w")
    file.write("Hello")
    # result = 10 / 0  # Even if error occurs
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    file.close()
    print("✅ File closed (cleanup done)")

# Getting error details
print("\n7️⃣  GETTING ERROR DETAILS")
print("-" * 60)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")

# Generic exception handler
print("\n8️⃣  GENERIC EXCEPTION HANDLER")
print("-" * 60)

try:
    # Some code that might fail
    numbers = [1, 2, 3]
    print(numbers[10])  # IndexError
except Exception as e:
    print(f"❌ Something went wrong: {e}")

# Specific before generic
print("\n9️⃣  SPECIFIC BEFORE GENERIC")
print("-" * 60)

try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ Specific: Division by zero")
except Exception as e:
    print(f"❌ Generic: {e}")

print()
