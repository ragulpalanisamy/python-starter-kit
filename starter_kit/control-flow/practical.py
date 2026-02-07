# ============================================
# PRACTICAL CONTROL FLOW EXAMPLES
# ============================================

print("=" * 60)
print("PRACTICAL CONTROL FLOW EXAMPLES")
print("=" * 60)

# Example 1: Menu system
print("\n1️⃣  MENU SYSTEM")
print("-" * 60)
while True:
    print("\n=== Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"Result: {a + b}")
    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"Result: {a - b}")
    elif choice == "3":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid option!")

# Example 2: FizzBuzz
print("\n2️⃣  FIZZBUZZ")
print("-" * 60)
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# Example 3: Prime number checker
print("\n3️⃣  PRIME NUMBER CHECKER")
print("-" * 60)
num = 17
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

print(f"{num} is {'prime' if is_prime else 'not prime'}")

# Example 4: Multiplication table
print("\n4️⃣  MULTIPLICATION TABLE")
print("-" * 60)
n = 5
print(f"Multiplication table of {n}:")
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")

# Example 5: Pattern printing
print("\n5️⃣  PATTERN PRINTING")
print("-" * 60)
rows = 5
for i in range(1, rows + 1):
    print("* " * i)

# Example 6: Sum of numbers
print("\n6️⃣  SUM OF NUMBERS")
print("-" * 60)
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# Example 7: Find max in list
print("\n7️⃣  FIND MAXIMUM")
print("-" * 60)
numbers = [45, 23, 89, 12, 67]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Numbers: {numbers}")
print(f"Maximum: {max_num}")

# Example 8: Count vowels
print("\n8️⃣  COUNT VOWELS")
print("-" * 60)
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Text: {text}")
print(f"Vowels: {count}")

# Example 9: Reverse a string
print("\n9️⃣  REVERSE STRING")
print("-" * 60)
text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(f"Original: {text}")
print(f"Reversed: {reversed_text}")

# Example 10: Shopping cart
print("\n🔟 SHOPPING CART")
print("-" * 60)
cart = {
    "apple": 50,
    "banana": 30,
    "mango": 80
}

total = 0
for item, price in cart.items():
    print(f"{item.capitalize()}: ₹{price}")
    total += price

print(f"Total: ₹{total}")

# Apply discount
if total > 100:
    discount = total * 0.1
    final = total - discount
    print(f"Discount (10%): ₹{discount}")
    print(f"Final amount: ₹{final}")

print()
