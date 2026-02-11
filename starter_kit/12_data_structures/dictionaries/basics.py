# ============================================
# DICTIONARY BASICS
# ============================================

print("=" * 60)
print("DICTIONARY BASICS")
print("=" * 60)

# Creating dictionaries
print("\n1️⃣  CREATING DICTIONARIES")
print("-" * 60)

# Empty dictionary
empty = {}
print(f"Empty: {empty}")

# Dictionary with values
user = {"name": "Ragul", "age": 25, "city": "Chennai"}
print(f"User: {user}")

# Accessing values
print("\n2️⃣  ACCESSING VALUES")
print("-" * 60)
print(f"Name: {user['name']}")
print(f"Age: {user.get('age')}")

# Adding/updating
print("\n3️⃣  ADDING/UPDATING")
print("-" * 60)
user["email"] = "ragul@example.com"
print(f"After adding email: {user}")

# Dictionary methods
print("\n4️⃣  DICTIONARY METHODS")
print("-" * 60)
print(f"Keys: {user.keys()}")
print(f"Values: {user.values()}")
print(f"Items: {user.items()}")

# Iterating
print("\n5️⃣  ITERATING")
print("-" * 60)
for key, value in user.items():
    print(f"  {key}: {value}")

print()
