# ============================================
# FILE HANDLING - PRACTICAL EXAMPLES
# ============================================

print("=" * 60)
print("FILE HANDLING - PRACTICAL EXAMPLES")
print("=" * 60)

import os
import json
import csv

# Example 1: Log file
print("\n1️⃣  LOG FILE")
print("-" * 60)

def write_log(message):
    """Append log message to file"""
    with open("app.log", "a") as file:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")

write_log("Application started")
write_log("User logged in")
write_log("Data processed")

print("Log entries:")
with open("app.log", "r") as file:
    print(file.read())

# Example 2: Configuration file
print("\n2️⃣  CONFIGURATION FILE")
print("-" * 60)

config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "app": {
        "debug": True,
        "version": "1.0.0"
    }
}

# Save config
with open("config.json", "w") as file:
    json.dump(config, file, indent=2)
print("✅ Config saved")

# Load config
with open("config.json", "r") as file:
    loaded_config = json.load(file)
    print(f"Database host: {loaded_config['database']['host']}")
    print(f"App version: {loaded_config['app']['version']}")

# Example 3: Student records (CSV)
print("\n3️⃣  STUDENT RECORDS (CSV)")
print("-" * 60)

students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"}
]

# Write CSV with headers
with open("students.csv", "w", newline='') as file:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
print("✅ Students saved to CSV")

# Read CSV
print("\nStudent records:")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"  {row['name']}: Age {row['age']}, Grade {row['grade']}")

# Example 4: Word counter
print("\n4️⃣  WORD COUNTER")
print("-" * 60)

# Create sample text file
with open("story.txt", "w") as file:
    file.write("Python is awesome. Python is powerful. Python is easy to learn.")

# Count words
with open("story.txt", "r") as file:
    content = file.read()
    words = content.split()
    word_count = {}
    
    for word in words:
        word = word.lower().strip('.,!?')
        word_count[word] = word_count.get(word, 0) + 1

print("Word frequency:")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")

# Example 5: File backup
print("\n5️⃣  FILE BACKUP")
print("-" * 60)

def backup_file(filename):
    """Create backup of file"""
    if os.path.exists(filename):
        backup_name = f"{filename}.backup"
        with open(filename, "r") as original:
            with open(backup_name, "w") as backup:
                backup.write(original.read())
        print(f"✅ Backup created: {backup_name}")
    else:
        print(f"❌ File not found: {filename}")

backup_file("config.json")

# Example 6: File search
print("\n6️⃣  FILE SEARCH")
print("-" * 60)

def search_in_file(filename, search_term):
    """Search for term in file"""
    try:
        with open(filename, "r") as file:
            for line_num, line in enumerate(file, 1):
                if search_term.lower() in line.lower():
                    print(f"  Line {line_num}: {line.strip()}")
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")

print(f"Searching for 'Python' in story.txt:")
search_in_file("story.txt", "Python")

# Example 7: Directory operations
print("\n7️⃣  DIRECTORY OPERATIONS")
print("-" * 60)

# Create directory
if not os.path.exists("data"):
    os.mkdir("data")
    print("✅ Created 'data' directory")

# List files in directory
print("\nFiles in current directory:")
for item in os.listdir("."):
    if os.path.isfile(item):
        size = os.path.getsize(item)
        print(f"  📄 {item} ({size} bytes)")

# Example 8: File copy
print("\n8️⃣  FILE COPY")
print("-" * 60)

def copy_file(source, destination):
    """Copy file from source to destination"""
    try:
        with open(source, "r") as src:
            with open(destination, "w") as dst:
                dst.write(src.read())
        print(f"✅ Copied {source} to {destination}")
    except FileNotFoundError:
        print(f"❌ Source file not found: {source}")

copy_file("config.json", "data/config_copy.json")

# Example 9: Line counter
print("\n9️⃣  LINE COUNTER")
print("-" * 60)

def count_lines(filename):
    """Count lines in file"""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            total = len(lines)
            non_empty = sum(1 for line in lines if line.strip())
            print(f"Total lines: {total}")
            print(f"Non-empty lines: {non_empty}")
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")

count_lines("story.txt")

# Example 10: File merge
print("\n🔟 FILE MERGE")
print("-" * 60)

# Create two files
with open("file1.txt", "w") as f:
    f.write("Content from file 1\n")

with open("file2.txt", "w") as f:
    f.write("Content from file 2\n")

# Merge files
with open("merged.txt", "w") as merged:
    for filename in ["file1.txt", "file2.txt"]:
        with open(filename, "r") as f:
            merged.write(f.read())

print("✅ Files merged")
print("Merged content:")
with open("merged.txt", "r") as f:
    print(f.read())

# Cleanup
print("\nCleaning up demo files...")
demo_files = [
    "app.log", "config.json", "students.csv", "story.txt",
    "config.json.backup", "file1.txt", "file2.txt", "merged.txt"
]

for filename in demo_files:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"✅ Deleted {filename}")

# Remove data directory
if os.path.exists("data"):
    for file in os.listdir("data"):
        os.remove(os.path.join("data", file))
    os.rmdir("data")
    print("✅ Deleted 'data' directory")

print()
