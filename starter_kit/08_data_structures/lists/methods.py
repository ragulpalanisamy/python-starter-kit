# ============================================
# LIST METHODS
# ============================================

print("=" * 60)
print("LIST METHODS")
print("=" * 60)

# append() - Add element to end
print("\n1️⃣  APPEND - Add to End")
print("-" * 60)
fruits = ["apple", "banana"]
print(f"Original: {fruits}")
fruits.append("mango")
print(f"After append('mango'): {fruits}")

# insert() - Add element at specific position
print("\n2️⃣  INSERT - Add at Position")
print("-" * 60)
fruits = ["apple", "mango"]
print(f"Original: {fruits}")
fruits.insert(1, "banana")  # Insert at index 1
print(f"After insert(1, 'banana'): {fruits}")

# extend() - Add multiple elements
print("\n3️⃣  EXTEND - Add Multiple")
print("-" * 60)
fruits = ["apple", "banana"]
more_fruits = ["mango", "orange"]
print(f"Original: {fruits}")
print(f"Adding: {more_fruits}")
fruits.extend(more_fruits)
print(f"After extend: {fruits}")

# remove() - Remove first occurrence
print("\n4️⃣  REMOVE - Remove by Value")
print("-" * 60)
fruits = ["apple", "banana", "mango", "banana"]
print(f"Original: {fruits}")
fruits.remove("banana")  # Removes first 'banana'
print(f"After remove('banana'): {fruits}")

# pop() - Remove and return element
print("\n5️⃣  POP - Remove by Index")
print("-" * 60)
fruits = ["apple", "banana", "mango"]
print(f"Original: {fruits}")
removed = fruits.pop()  # Remove last
print(f"Popped: {removed}")
print(f"After pop(): {fruits}")

removed = fruits.pop(0)  # Remove at index 0
print(f"Popped at index 0: {removed}")
print(f"After pop(0): {fruits}")

# clear() - Remove all elements
print("\n6️⃣  CLEAR - Remove All")
print("-" * 60)
fruits = ["apple", "banana", "mango"]
print(f"Original: {fruits}")
fruits.clear()
print(f"After clear(): {fruits}")

# index() - Find position of element
print("\n7️⃣  INDEX - Find Position")
print("-" * 60)
fruits = ["apple", "banana", "mango"]
print(f"Fruits: {fruits}")
print(f"Index of 'banana': {fruits.index('banana')}")
print(f"Index of 'mango': {fruits.index('mango')}")

# count() - Count occurrences
print("\n8️⃣  COUNT - Count Occurrences")
print("-" * 60)
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"Numbers: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Count of 5: {numbers.count(5)}")

# sort() - Sort in place
print("\n9️⃣  SORT - Sort In Place")
print("-" * 60)
numbers = [5, 2, 8, 1, 9]
print(f"Original: {numbers}")
numbers.sort()
print(f"After sort(): {numbers}")

numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# sorted() - Return sorted copy
print("\n🔟 SORTED - Return Sorted Copy")
print("-" * 60)
numbers = [5, 2, 8, 1, 9]
print(f"Original: {numbers}")
sorted_numbers = sorted(numbers)
print(f"Sorted copy: {sorted_numbers}")
print(f"Original unchanged: {numbers}")

# reverse() - Reverse in place
print("\n1️⃣1️⃣  REVERSE - Reverse In Place")
print("-" * 60)
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
numbers.reverse()
print(f"After reverse(): {numbers}")

# copy() - Create shallow copy
print("\n1️⃣2️⃣  COPY - Create Copy")
print("-" * 60)
original = [1, 2, 3]
copy = original.copy()
print(f"Original: {original}")
print(f"Copy: {copy}")

copy.append(4)
print(f"After modifying copy:")
print(f"Original: {original}")
print(f"Copy: {copy}")

print()
