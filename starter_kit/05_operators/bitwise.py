# ============================================
# BITWISE OPERATORS
# ============================================

print("=" * 50)
print("BITWISE OPERATORS")
print("=" * 50)

a = 10  # Binary: 1010
b = 4   # Binary: 0100

print(f"\na = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})\n")

# Bitwise AND (&)
result = a & b
print(f"{a} & {b} = {result} (binary: {bin(result)})")

# Bitwise OR (|)
result = a | b
print(f"{a} | {b} = {result} (binary: {bin(result)})")

# Bitwise XOR (^)
result = a ^ b
print(f"{a} ^ {b} = {result} (binary: {bin(result)})")

# Bitwise NOT (~)
result = ~a
print(f"~{a} = {result} (binary: {bin(result)})")

# Left shift (<<)
result = a << 2
print(f"{a} << 2 = {result} (binary: {bin(result)})")

# Right shift (>>)
result = a >> 2
print(f"{a} >> 2 = {result} (binary: {bin(result)})")

print()

# Practical Examples
print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Multiply/Divide by powers of 2 using shifts
num = 5
print(f"\nOriginal number: {num}")

doubled = num << 1  # Multiply by 2
print(f"Multiply by 2 (left shift): {doubled}")

quadrupled = num << 2  # Multiply by 4
print(f"Multiply by 4 (left shift): {quadrupled}")

halved = num >> 1  # Divide by 2
print(f"Divide by 2 (right shift): {halved}")

# Check if number is even or odd using bitwise AND
number = 17
if number & 1:
    print(f"\n{number} is ODD (last bit is 1)")
else:
    print(f"\n{number} is EVEN (last bit is 0)")

# Swap two numbers using XOR
x = 15
y = 25
print(f"\nBefore swap: x = {x}, y = {y}")

x = x ^ y
y = x ^ y
x = x ^ y

print(f"After swap: x = {x}, y = {y}")

print()
