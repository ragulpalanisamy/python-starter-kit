# ============================================
# STRING METHODS
# ============================================

print("=" * 60)
print("STRING METHODS")
print("=" * 60)

text = "  Hello, World!  "

# Case conversion
print("\n1️⃣  CASE CONVERSION")
print("-" * 60)
print(f"Original: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"swapcase(): '{text.swapcase()}'")

# Whitespace removal
print("\n2️⃣  WHITESPACE REMOVAL")
print("-" * 60)
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")

# Search methods
print("\n3️⃣  SEARCH METHODS")
print("-" * 60)
sentence = "Python is awesome. Python is powerful."
print(f"String: {sentence}")
print(f"find('Python'): {sentence.find('Python')}")
print(f"find('Java'): {sentence.find('Java')}")  # -1 if not found
print(f"index('awesome'): {sentence.index('awesome')}")
print(f"count('Python'): {sentence.count('Python')}")
print(f"startswith('Python'): {sentence.startswith('Python')}")
print(f"endswith('powerful.'): {sentence.endswith('powerful.')}")

# Replace
print("\n4️⃣  REPLACE")
print("-" * 60)
original = "I love Java"
replaced = original.replace("Java", "Python")
print(f"Original: {original}")
print(f"Replaced: {replaced}")

# Split and Join
print("\n5️⃣  SPLIT & JOIN")
print("-" * 60)
csv = "apple,banana,mango"
fruits = csv.split(',')
print(f"Original: {csv}")
print(f"split(','): {fruits}")

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"List: {words}")
print(f"join(): {sentence}")

# Validation methods
print("\n6️⃣  VALIDATION METHODS")
print("-" * 60)
print(f"'hello'.isalpha(): {'hello'.isalpha()}")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'hello123'.isalnum(): {'hello123'.isalnum()}")
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'Hello World'.istitle(): {'Hello World'.istitle()}")
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")
print(f"'hello'.islower(): {'hello'.islower()}")

print()
