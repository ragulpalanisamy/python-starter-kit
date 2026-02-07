# ============================================
# WHILE LOOPS
# ============================================

print("=" * 60)
print("WHILE LOOPS")
print("=" * 60)

# Basic while loop
print("\n1️⃣  BASIC WHILE LOOP")
print("-" * 60)
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While with condition
print("\n2️⃣  WHILE WITH CONDITION")
print("-" * 60)
password = ""
attempts = 0
max_attempts = 3

while password != "secret" and attempts < max_attempts:
    password = input(f"Enter password (attempt {attempts + 1}/{max_attempts}): ")
    attempts += 1
    
    if password == "secret":
        print("✅ Access granted!")
    elif attempts >= max_attempts:
        print("❌ Too many attempts!")
    else:
        print("❌ Wrong password, try again")

# Infinite loop with break
print("\n3️⃣  INFINITE LOOP WITH BREAK")
print("-" * 60)
counter = 0
while True:
    print(f"Counter: {counter}")
    counter += 1
    if counter >= 3:
        print("Breaking out of loop!")
        break

# While with continue
print("\n4️⃣  WHILE WITH CONTINUE")
print("-" * 60)
num = 0
while num < 5:
    num += 1
    if num == 3:
        print(f"Skipping {num}")
        continue
    print(f"Number: {num}")

# While-else
print("\n5️⃣  WHILE-ELSE")
print("-" * 60)
n = 0
while n < 3:
    print(f"n = {n}")
    n += 1
else:
    print("Loop completed normally (no break)")

# Practical example: Input validation
print("\n6️⃣  PRACTICAL: INPUT VALIDATION")
print("-" * 60)
while True:
    age_input = input("Enter your age (or 'quit' to exit): ")
    
    if age_input.lower() == 'quit':
        print("Exiting...")
        break
    
    if age_input.isdigit():
        age = int(age_input)
        if 0 < age < 120:
            print(f"✅ Valid age: {age}")
            break
        else:
            print("❌ Age must be between 1 and 119")
    else:
        print("❌ Please enter a valid number")

print()
