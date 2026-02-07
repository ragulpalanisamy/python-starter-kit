# ============================================
# IDENTITY OPERATORS
# ============================================

print("=" * 50)
print("IDENTITY OPERATORS")
print("=" * 50)

# is - Returns True if both variables point to the same object
# is not - Returns True if both variables point to different objects

# Integer example (small integers are cached)
a = 10
b = 10
c = 20

print(f"\na = {a}, b = {b}, c = {c}")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}\n")

result = a is b
print(f"a is b → {result} (same object)")

result = a is c
print(f"a is c → {result} (different objects)")

result = a is not c
print(f"a is not c → {result}")

# List example (different objects even with same values)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"\nlist1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")
print(f"id(list1) = {id(list1)}")
print(f"id(list2) = {id(list2)}")
print(f"id(list3) = {id(list3)}\n")

result = list1 is list2
print(f"list1 is list2 → {result} (different objects)")

result = list1 == list2
print(f"list1 == list2 → {result} (same values)")

result = list1 is list3
print(f"list1 is list3 → {result} (same object)")

# None comparison
value = None
print(f"\nvalue = {value}\n")

result = value is None
print(f"value is None → {result}")

result = value is not None
print(f"value is not None → {result}")

print()

# Practical Examples
print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Check if variable is None
user_input = None

if user_input is None:
    print("\n⚠️ No input provided")
else:
    print(f"\n✅ Input received: {user_input}")

# Check if two variables reference the same list
original_list = [1, 2, 3]
copied_list = original_list.copy()
reference_list = original_list

print(f"\noriginal_list = {original_list}")
print(f"copied_list = {copied_list}")
print(f"reference_list = original_list")

if original_list is copied_list:
    print("original_list and copied_list: Same object")
else:
    print("original_list and copied_list: Different objects ✓")

if original_list is reference_list:
    print("original_list and reference_list: Same object ✓")
else:
    print("original_list and reference_list: Different objects")

# Modifying to show the difference
original_list.append(4)
print(f"\nAfter original_list.append(4):")
print(f"original_list = {original_list}")
print(f"copied_list = {copied_list} (unchanged)")
print(f"reference_list = {reference_list} (changed)")

# Boolean singleton check
is_active = True
is_enabled = True

if is_active is True:
    print(f"\n✅ Status is active")

# Better practice: direct boolean check
if is_active:
    print(f"✅ Status is active (better way)")

print()
