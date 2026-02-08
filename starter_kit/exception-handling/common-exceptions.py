# ============================================
# COMMON EXCEPTIONS
# ============================================

print("=" * 60)
print("COMMON EXCEPTIONS")
print("=" * 60)

# ZeroDivisionError
print("\n1️⃣  ZeroDivisionError")
print("-" * 60)

try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")

# ValueError
print("\n2️⃣  ValueError")
print("-" * 60)

try:
    number = int("abc")  # Can't convert "abc" to int
except ValueError:
    print("❌ Invalid value for conversion!")

# TypeError
print("\n3️⃣  TypeError")
print("-" * 60)

try:
    result = "10" + 5  # Can't add string and int
except TypeError:
    print("❌ Cannot add string and number!")

# IndexError
print("\n4️⃣  IndexError")
print("-" * 60)

try:
    numbers = [1, 2, 3]
    print(numbers[10])  # Index doesn't exist
except IndexError:
    print("❌ Index out of range!")

# KeyError
print("\n5️⃣  KeyError")
print("-" * 60)

try:
    user = {"name": "Ragul", "age": 25}
    print(user["email"])  # Key doesn't exist
except KeyError:
    print("❌ Key not found in dictionary!")

# FileNotFoundError
print("\n6️⃣  FileNotFoundError")
print("-" * 60)

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("❌ File not found!")

# AttributeError
print("\n7️⃣  AttributeError")
print("-" * 60)

try:
    text = "hello"
    text.append("world")  # Strings don't have append()
except AttributeError:
    print("❌ Attribute doesn't exist!")

# NameError
print("\n8️⃣  NameError")
print("-" * 60)

try:
    print(undefined_variable)  # Variable not defined
except NameError:
    print("❌ Variable not defined!")

# ImportError
print("\n9️⃣  ImportError")
print("-" * 60)

try:
    import nonexistent_module
except ImportError:
    print("❌ Module not found!")

# Summary
print("\n🔟 COMMON EXCEPTIONS SUMMARY")
print("-" * 60)
print("ZeroDivisionError  - Division by zero")
print("ValueError         - Invalid value")
print("TypeError          - Wrong type")
print("IndexError         - Invalid index")
print("KeyError           - Key not found")
print("FileNotFoundError  - File doesn't exist")
print("AttributeError     - Attribute doesn't exist")
print("NameError          - Variable not defined")
print("ImportError        - Module not found")

print()
