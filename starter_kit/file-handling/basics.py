# ============================================
# FILE HANDLING BASICS
# ============================================

print("=" * 60)
print("FILE HANDLING BASICS")
print("=" * 60)

# Writing to a file
print("\n1️⃣  WRITING TO FILE")
print("-" * 60)

# Method 1: write() - overwrites file
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")
print("✅ Written to sample.txt")

# Method 2: writelines() - write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("lines.txt", "w") as file:
    file.writelines(lines)
print("✅ Written to lines.txt")

# Reading from a file
print("\n2️⃣  READING FROM FILE")
print("-" * 60)

# Method 1: read() - read entire file
with open("sample.txt", "r") as file:
    content = file.read()
    print("Full content:")
    print(content)

# Method 2: readline() - read one line at a time
print("Reading line by line:")
with open("sample.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")

# Method 3: readlines() - read all lines into list
with open("sample.txt", "r") as file:
    all_lines = file.readlines()
    print(f"\nAll lines: {all_lines}")

# Method 4: Loop through file (best for large files)
print("\nLooping through file:")
with open("sample.txt", "r") as file:
    for line in file:
        print(f"  {line.strip()}")

# Appending to a file
print("\n3️⃣  APPENDING TO FILE")
print("-" * 60)

with open("sample.txt", "a") as file:
    file.write("This is appended line\n")
print("✅ Appended to sample.txt")

# Read updated file
with open("sample.txt", "r") as file:
    print("Updated content:")
    print(file.read())

# File modes
print("\n4️⃣  FILE MODES")
print("-" * 60)
print("'r'  - Read (default)")
print("'w'  - Write (overwrites)")
print("'a'  - Append")
print("'r+' - Read and Write")
print("'w+' - Write and Read (overwrites)")
print("'a+' - Append and Read")
print("'rb' - Read binary")
print("'wb' - Write binary")

# Checking if file exists
print("\n5️⃣  CHECKING FILE EXISTS")
print("-" * 60)

import os

if os.path.exists("sample.txt"):
    print("✅ sample.txt exists")
else:
    print("❌ sample.txt does not exist")

# File information
print("\n6️⃣  FILE INFORMATION")
print("-" * 60)

if os.path.exists("sample.txt"):
    size = os.path.getsize("sample.txt")
    print(f"File size: {size} bytes")
    
    # Check if it's a file or directory
    print(f"Is file: {os.path.isfile('sample.txt')}")
    print(f"Is directory: {os.path.isdir('sample.txt')}")

# Error handling
print("\n7️⃣  ERROR HANDLING")
print("-" * 60)

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("❌ File not found!")
except PermissionError:
    print("❌ Permission denied!")
except Exception as e:
    print(f"❌ Error: {e}")

# Working with CSV files
print("\n8️⃣  CSV FILES")
print("-" * 60)

import csv

# Write CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "NYC"],
    ["Bob", "30", "LA"],
    ["Charlie", "35", "Chicago"]
]

with open("users.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("✅ Written to users.csv")

# Read CSV
print("\nReading CSV:")
with open("users.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"  {row}")

# Working with JSON files
print("\n9️⃣  JSON FILES")
print("-" * 60)

import json

# Write JSON
user_data = {
    "name": "Ragul",
    "age": 25,
    "city": "Chennai",
    "skills": ["Python", "JavaScript", "SQL"]
}

with open("user.json", "w") as file:
    json.dump(user_data, file, indent=2)
print("✅ Written to user.json")

# Read JSON
with open("user.json", "r") as file:
    loaded_data = json.load(file)
    print(f"Loaded data: {loaded_data}")
    print(f"Name: {loaded_data['name']}")
    print(f"Skills: {loaded_data['skills']}")

# Deleting files
print("\n🔟 DELETING FILES")
print("-" * 60)

# Delete a file
if os.path.exists("lines.txt"):
    os.remove("lines.txt")
    print("✅ Deleted lines.txt")

# Clean up
print("\nCleaning up demo files...")
for filename in ["sample.txt", "users.csv", "user.json"]:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"✅ Deleted {filename}")

print()
