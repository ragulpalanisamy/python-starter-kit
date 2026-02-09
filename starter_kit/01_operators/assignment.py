# ============================================
# ASSIGNMENT OPERATORS
# ============================================

print("=" * 50)
print("ASSIGNMENT OPERATORS")
print("=" * 50)

# Simple assignment (=)
x = 10
print(f"\nx = 10 → x = {x}")

# Add and assign (+=)
x += 5  # Same as: x = x + 5
print(f"x += 5 → x = {x}")

# Subtract and assign (-=)
x -= 3  # Same as: x = x - 3
print(f"x -= 3 → x = {x}")

# Multiply and assign (*=)
x *= 2  # Same as: x = x * 2
print(f"x *= 2 → x = {x}")

# Divide and assign (/=)
x /= 4  # Same as: x = x / 4
print(f"x /= 4 → x = {x}")

# Floor divide and assign (//=)
x = 25
x //= 4  # Same as: x = x // 4
print(f"\nx = 25")
print(f"x //= 4 → x = {x}")

# Modulus and assign (%=)
x = 17
x %= 5  # Same as: x = x % 5
print(f"\nx = 17")
print(f"x %= 5 → x = {x}")

# Exponent and assign (**=)
x = 3
x **= 3  # Same as: x = x ** 3
print(f"\nx = 3")
print(f"x **= 3 → x = {x}")

print()

# Practical Examples
print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Shopping cart total
cart_total = 0
print(f"\nCart Total: ₹{cart_total}")

cart_total += 299  # Add item 1
print(f"Added item (₹299): ₹{cart_total}")

cart_total += 499  # Add item 2
print(f"Added item (₹499): ₹{cart_total}")

cart_total -= 100  # Apply discount
print(f"Applied discount (₹100): ₹{cart_total}")

# Score counter in a game
score = 0
print(f"\n🎮 Game Score: {score}")

score += 10  # Collected coin
print(f"Collected coin (+10): {score}")

score += 50  # Defeated enemy
print(f"Defeated enemy (+50): {score}")

score *= 2  # Double points bonus
print(f"Double points bonus (×2): {score}")

# Bank balance
balance = 5000
print(f"\n💰 Bank Balance: ₹{balance}")

balance += 2000  # Salary credited
print(f"Salary credited (+₹2000): ₹{balance}")

balance -= 1500  # Paid rent
print(f"Paid rent (-₹1500): ₹{balance}")

print()
