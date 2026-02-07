# ============================================
# PRACTICAL STRING EXAMPLES
# ============================================

print("=" * 60)
print("PRACTICAL STRING EXAMPLES")
print("=" * 60)

# Example 1: Email validation
print("\n1️⃣  EMAIL VALIDATION")
print("-" * 60)
email = "ragul@example.com"
if "@" in email and "." in email.split("@")[1]:
    print(f"✅ Valid email: {email}")
else:
    print(f"❌ Invalid email: {email}")

# Example 2: Password strength check
print("\n2️⃣  PASSWORD STRENGTH")
print("-" * 60)
password = "Secret@123"
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)
is_long = len(password) >= 8

if all([has_upper, has_lower, has_digit, has_special, is_long]):
    print(f"✅ Strong password")
else:
    print(f"❌ Weak password")
    print(f"   Length ≥ 8: {is_long}")
    print(f"   Uppercase: {has_upper}")
    print(f"   Lowercase: {has_lower}")
    print(f"   Digit: {has_digit}")
    print(f"   Special char: {has_special}")

# Example 3: Name formatting
print("\n3️⃣  NAME FORMATTING")
print("-" * 60)
full_name = "  ragul PALANISAMY  "
formatted = full_name.strip().title()
print(f"Original: '{full_name}'")
print(f"Formatted: '{formatted}'")

# Example 4: URL slug generation
print("\n4️⃣  URL SLUG GENERATION")
print("-" * 60)
title = "Python String Methods Tutorial"
slug = title.lower().replace(" ", "-")
print(f"Title: {title}")
print(f"Slug: {slug}")

# Example 5: Extract domain from email
print("\n5️⃣  EXTRACT DOMAIN FROM EMAIL")
print("-" * 60)
email = "user@company.com"
domain = email.split("@")[1]
print(f"Email: {email}")
print(f"Domain: {domain}")

# Example 6: Reverse words in a sentence
print("\n6️⃣  REVERSE WORDS")
print("-" * 60)
sentence = "Hello World Python"
reversed_words = " ".join(sentence.split()[::-1])
print(f"Original: {sentence}")
print(f"Reversed: {reversed_words}")

# Example 7: Count vowels
print("\n7️⃣  COUNT VOWELS")
print("-" * 60)
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"Text: {text}")
print(f"Vowels: {count}")

# Example 8: Remove duplicates while preserving order
print("\n8️⃣  REMOVE DUPLICATE CHARACTERS")
print("-" * 60)
text = "programming"
unique = "".join(dict.fromkeys(text))
print(f"Original: {text}")
print(f"Unique: {unique}")

# Example 9: Check palindrome
print("\n9️⃣  PALINDROME CHECK")
print("-" * 60)
word = "radar"
is_palindrome = word == word[::-1]
print(f"Word: {word}")
print(f"Is palindrome: {is_palindrome}")

# Example 10: Mask credit card
print("\n🔟 MASK CREDIT CARD")
print("-" * 60)
card = "1234567890123456"
masked = "*" * 12 + card[-4:]
print(f"Original: {card}")
print(f"Masked: {masked}")

print()
