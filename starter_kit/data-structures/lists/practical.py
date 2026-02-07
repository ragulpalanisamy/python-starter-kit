# ============================================
# PRACTICAL LIST EXAMPLES
# ============================================

print("=" * 60)
print("PRACTICAL LIST EXAMPLES")
print("=" * 60)

# Example 1: Shopping cart
print("\n1️⃣  SHOPPING CART")
print("-" * 60)
cart = []

# Add items
cart.append({"item": "Apple", "price": 50, "quantity": 3})
cart.append({"item": "Banana", "price": 30, "quantity": 5})
cart.append({"item": "Mango", "price": 80, "quantity": 2})

print("Cart items:")
for item in cart:
    subtotal = item["price"] * item["quantity"]
    print(f"  {item['item']}: ₹{item['price']} × {item['quantity']} = ₹{subtotal}")

total = sum(item["price"] * item["quantity"] for item in cart)
print(f"Total: ₹{total}")

# Example 2: Grade management
print("\n2️⃣  GRADE MANAGEMENT")
print("-" * 60)
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78},
    {"name": "David", "marks": 95}
]

# Sort by marks
sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)
print("Students sorted by marks:")
for i, student in enumerate(sorted_students, 1):
    print(f"  {i}. {student['name']}: {student['marks']}")

# Find top scorer
top_student = max(students, key=lambda x: x["marks"])
print(f"\nTop scorer: {top_student['name']} ({top_student['marks']} marks)")

# Calculate average
avg_marks = sum(s["marks"] for s in students) / len(students)
print(f"Average marks: {avg_marks:.2f}")

# Example 3: To-do list
print("\n3️⃣  TO-DO LIST")
print("-" * 60)
todos = []

# Add tasks
todos.append({"task": "Buy groceries", "done": False})
todos.append({"task": "Complete assignment", "done": False})
todos.append({"task": "Call dentist", "done": True})

print("To-do list:")
for i, todo in enumerate(todos, 1):
    status = "✅" if todo["done"] else "❌"
    print(f"  {i}. {status} {todo['task']}")

# Mark task as done
todos[1]["done"] = True
print("\nAfter completing task 2:")
for i, todo in enumerate(todos, 1):
    status = "✅" if todo["done"] else "❌"
    print(f"  {i}. {status} {todo['task']}")

# Example 4: Contact list
print("\n4️⃣  CONTACT LIST")
print("-" * 60)
contacts = [
    {"name": "Alice", "phone": "1234567890", "email": "alice@example.com"},
    {"name": "Bob", "phone": "9876543210", "email": "bob@example.com"}
]

# Search by name
search_name = "Alice"
found = [c for c in contacts if c["name"].lower() == search_name.lower()]
if found:
    contact = found[0]
    print(f"Found: {contact['name']}")
    print(f"  Phone: {contact['phone']}")
    print(f"  Email: {contact['email']}")

# Example 5: Inventory management
print("\n5️⃣  INVENTORY MANAGEMENT")
print("-" * 60)
inventory = [
    {"product": "Laptop", "stock": 5, "price": 50000},
    {"product": "Mouse", "stock": 20, "price": 500},
    {"product": "Keyboard", "stock": 0, "price": 1500}
]

print("Inventory:")
for item in inventory:
    status = "In Stock" if item["stock"] > 0 else "Out of Stock"
    print(f"  {item['product']}: {item['stock']} units - {status}")

# Low stock alert
low_stock = [item for item in inventory if 0 < item["stock"] < 10]
if low_stock:
    print("\n⚠️  Low stock alert:")
    for item in low_stock:
        print(f"  {item['product']}: {item['stock']} units")

# Example 6: Number analysis
print("\n6️⃣  NUMBER ANALYSIS")
print("-" * 60)
numbers = [12, 45, 23, 67, 34, 89, 15, 56]
print(f"Numbers: {numbers}")

# Separate even and odd
evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]
print(f"Even: {evens}")
print(f"Odd: {odds}")

# Numbers greater than 50
above_50 = [n for n in numbers if n > 50]
print(f"Above 50: {above_50}")

# Example 7: Word frequency
print("\n7️⃣  WORD FREQUENCY")
print("-" * 60)
text = "hello world hello python world hello"
words = text.split()
print(f"Text: {text}")

# Count frequency
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word frequency:")
for word, count in word_count.items():
    print(f"  {word}: {count}")

# Example 8: Remove items from list
print("\n8️⃣  REMOVE ITEMS")
print("-" * 60)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {numbers}")

# Remove all even numbers
numbers = [n for n in numbers if n % 2 != 0]
print(f"After removing evens: {numbers}")

# Example 9: Merge and sort lists
print("\n9️⃣  MERGE AND SORT")
print("-" * 60)
list1 = [3, 1, 4, 1, 5]
list2 = [9, 2, 6, 5, 3]
print(f"List 1: {list1}")
print(f"List 2: {list2}")

# Merge
merged = list1 + list2
print(f"Merged: {merged}")

# Sort
merged.sort()
print(f"Sorted: {merged}")

# Remove duplicates and sort
unique_sorted = sorted(list(set(merged)))
print(f"Unique sorted: {unique_sorted}")

# Example 10: Matrix operations
print("\n🔟 MATRIX OPERATIONS")
print("-" * 60)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Sum of all elements
total = sum(sum(row) for row in matrix)
print(f"Sum of all elements: {total}")

# Get diagonal
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(f"Diagonal: {diagonal}")

# Transpose
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Transpose:")
for row in transpose:
    print(f"  {row}")

print()
