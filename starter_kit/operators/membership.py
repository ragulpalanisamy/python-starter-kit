# ============================================
# MEMBERSHIP OPERATORS
# ============================================

print("=" * 50)
print("MEMBERSHIP OPERATORS")
print("=" * 50)

# in - Returns True if value exists in sequence
# not in - Returns True if value does not exist in sequence

# List example
fruits = ["apple", "banana", "mango", "orange"]
print(f"\nfruits = {fruits}\n")

result = "banana" in fruits
print(f"'banana' in fruits → {result}")

result = "grape" in fruits
print(f"'grape' in fruits → {result}")

result = "grape" not in fruits
print(f"'grape' not in fruits → {result}")

# String example
text = "Hello, World!"
print(f"\ntext = '{text}'\n")

result = "World" in text
print(f"'World' in text → {result}")

result = "Python" in text
print(f"'Python' in text → {result}")

result = "Python" not in text
print(f"'Python' not in text → {result}")

# Tuple example
numbers = (1, 2, 3, 4, 5)
print(f"\nnumbers = {numbers}\n")

result = 3 in numbers
print(f"3 in numbers → {result}")

result = 10 in numbers
print(f"10 in numbers → {result}")

# Dictionary example (checks keys by default)
user = {"name": "Ragul", "age": 25, "city": "Chennai"}
print(f"\nuser = {user}\n")

result = "name" in user
print(f"'name' in user → {result}")

result = "email" in user
print(f"'email' in user → {result}")

print()

# Practical Examples
print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Check if user has permission
permissions = ["read", "write", "delete"]
action = "write"

if action in permissions:
    print(f"\n✅ Permission granted for '{action}'")
else:
    print(f"\n❌ Permission denied for '{action}'")

# Email validation
email = "ragul@example.com"
if "@" in email and "." in email:
    print(f"\n✅ Valid email format: {email}")
else:
    print(f"\n❌ Invalid email format: {email}")

# Check if word is in banned list
banned_words = ["spam", "hack", "virus"]
message = "This is a normal message"

has_banned = False
for word in banned_words:
    if word in message.lower():
        has_banned = True
        break

if has_banned:
    print(f"\n❌ Message contains banned words")
else:
    print(f"\n✅ Message is clean")

# Check if user is premium member
premium_users = ["ragul", "john", "alice"]
current_user = "ragul"

if current_user in premium_users:
    print(f"\n🌟 Welcome Premium Member: {current_user}")
else:
    print(f"\n👤 Regular User: {current_user}")

# File extension check
filename = "document.pdf"
allowed_extensions = [".pdf", ".doc", ".docx"]

has_valid_extension = False
for ext in allowed_extensions:
    if ext in filename:
        has_valid_extension = True
        break

if has_valid_extension:
    print(f"\n✅ File type allowed: {filename}")
else:
    print(f"\n❌ File type not allowed: {filename}")

print()
