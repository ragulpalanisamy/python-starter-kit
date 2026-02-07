# ============================================
# STRING BASICS
# ============================================

print("=" * 60)
print("STRING BASICS")
print("=" * 60)

# Creating strings
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''Multiple
lines
string'''

print(f"Single quotes: {single_quote}")
print(f"Double quotes: {double_quote}")
print(f"Triple quotes:\n{triple_quote}")

print()

# String concatenation
first_name = "Ragul"
last_name = "Palanisamy"
full_name = first_name + " " + last_name
print(f"Concatenation: {full_name}")

# String repetition
repeat = "Ha" * 3
print(f"Repetition: {repeat}")

# String length
text = "Python"
print(f"Length of '{text}': {len(text)}")

print()

# String indexing (0-based)
word = "Python"
print(f"String: {word}")
print(f"First character: {word[0]}")
print(f"Last character: {word[-1]}")
print(f"Second character: {word[1]}")

print()

# String slicing [start:end:step]
text = "Hello, World!"
print(f"String: {text}")
print(f"[0:5]: {text[0:5]}")      # Hello
print(f"[7:]: {text[7:]}")        # World!
print(f"[:5]: {text[:5]}")        # Hello
print(f"[::2]: {text[::2]}")      # Hlo ol!
print(f"[::-1]: {text[::-1]}")    # Reverse

print()
