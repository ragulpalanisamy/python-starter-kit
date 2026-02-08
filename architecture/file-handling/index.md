# File Handling - Simple Guide

## Table of Contents

1. [File Basics](#basics)
2. [Reading Files](#reading)
3. [Writing Files](#writing)
4. [File Modes](#modes)
5. [Working with CSV](#csv)
6. [Working with JSON](#json)
7. [Practical Examples](#practical)

---

## 🖼️ Visual Architecture

![Python file handling Diagram](file-handling.png)

## File Basics {#basics}

### Opening and Closing Files

**Best practice:** Use `with` statement (automatically closes file)

```python
# ✅ GOOD - Automatically closes file
with open("file.txt", "r") as file:
    content = file.read()

# ❌ BAD - Must manually close
file = open("file.txt", "r")
content = file.read()
file.close()  # Easy to forget!
```

### Why Use `with`?

✅ Automatically closes file  
✅ Works even if error occurs  
✅ Cleaner code

---

## Reading Files {#reading}

### Method 1: read() - Read Entire File

```python
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
```

**Use when:** File is small, you need all content at once

### Method 2: readline() - Read One Line

```python
with open("file.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)
```

**Use when:** You need to read lines one by one

### Method 3: readlines() - Read All Lines into List

```python
with open("file.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # ['Line 1\n', 'Line 2\n', 'Line 3\n']
```

**Use when:** You need all lines as a list

### Method 4: Loop Through File (Best for Large Files)

```python
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())  # Remove \n
```

**Use when:** File is large, process line by line

### Comparison

| Method        | Returns                | Memory | Best For         |
| ------------- | ---------------------- | ------ | ---------------- |
| `read()`      | String                 | High   | Small files      |
| `readline()`  | String (one line)      | Low    | Line by line     |
| `readlines()` | List of strings        | High   | All lines needed |
| Loop          | String (per iteration) | Low    | Large files      |

---

## Writing Files {#writing}

### Method 1: write() - Write String

```python
with open("file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
```

⚠️ **Warning:** `"w"` mode **overwrites** existing file!

### Method 2: writelines() - Write List of Strings

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("file.txt", "w") as file:
    file.writelines(lines)
```

### Appending to File

```python
with open("file.txt", "a") as file:
    file.write("This is appended\n")
```

✅ `"a"` mode **adds** to end of file (doesn't overwrite)

---

## File Modes {#modes}

| Mode   | Meaning       | Creates if Missing? | Overwrites? |
| ------ | ------------- | ------------------- | ----------- |
| `"r"`  | Read          | ❌ No (Error)       | -           |
| `"w"`  | Write         | ✅ Yes              | ✅ Yes      |
| `"a"`  | Append        | ✅ Yes              | ❌ No       |
| `"r+"` | Read + Write  | ❌ No               | ❌ No       |
| `"w+"` | Write + Read  | ✅ Yes              | ✅ Yes      |
| `"a+"` | Append + Read | ✅ Yes              | ❌ No       |
| `"rb"` | Read binary   | ❌ No               | -           |
| `"wb"` | Write binary  | ✅ Yes              | ✅ Yes      |

### Common Modes

```python
# Read only
with open("file.txt", "r") as file:
    content = file.read()

# Write (overwrites)
with open("file.txt", "w") as file:
    file.write("New content")

# Append (adds to end)
with open("file.txt", "a") as file:
    file.write("Appended content")
```

---

## Working with CSV {#csv}

CSV = Comma-Separated Values (like Excel files)

### Writing CSV

```python
import csv

# Method 1: Write rows
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "NYC"],
    ["Bob", "30", "LA"]
]

with open("users.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

### Reading CSV

```python
import csv

with open("users.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ['Alice', '25', 'NYC']
```

### CSV with Dictionary

```python
import csv

# Write
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"}
]

with open("students.csv", "w", newline='') as file:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write column names
    writer.writerows(students)

# Read
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"], row["grade"])
```

---

## Working with JSON {#json}

JSON = JavaScript Object Notation (like Python dictionaries)

### Writing JSON

```python
import json

user = {
    "name": "Ragul",
    "age": 25,
    "city": "Chennai",
    "skills": ["Python", "JavaScript"]
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=2)  # indent=2 for pretty formatting
```

### Reading JSON

```python
import json

with open("user.json", "r") as file:
    user = json.load(file)
    print(user["name"])     # Ragul
    print(user["skills"])   # ['Python', 'JavaScript']
```

### JSON String Conversion

```python
import json

# Python dict → JSON string
user = {"name": "Ragul", "age": 25}
json_string = json.dumps(user)
print(json_string)  # '{"name": "Ragul", "age": 25}'

# JSON string → Python dict
data = json.loads(json_string)
print(data["name"])  # Ragul
```

---

## Practical Examples {#practical}

### Example 1: Log File

```python
def write_log(message):
    """Append log message with timestamp"""
    from datetime import datetime
    with open("app.log", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")

write_log("Application started")
write_log("User logged in")
```

### Example 2: Configuration File

```python
import json

# Save config
config = {
    "database": {"host": "localhost", "port": 5432},
    "app": {"debug": True, "version": "1.0.0"}
}

with open("config.json", "w") as file:
    json.dump(config, file, indent=2)

# Load config
with open("config.json", "r") as file:
    config = json.load(file)
    print(config["database"]["host"])  # localhost
```

### Example 3: Word Counter

```python
with open("story.txt", "r") as file:
    content = file.read()
    words = content.split()

    word_count = {}
    for word in words:
        word = word.lower().strip('.,!?')
        word_count[word] = word_count.get(word, 0) + 1

# Print most common words
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")
```

### Example 4: File Backup

```python
import os

def backup_file(filename):
    """Create backup of file"""
    if os.path.exists(filename):
        backup_name = f"{filename}.backup"
        with open(filename, "r") as original:
            with open(backup_name, "w") as backup:
                backup.write(original.read())
        print(f"✅ Backup created: {backup_name}")

backup_file("important.txt")
```

### Example 5: Search in File

```python
def search_in_file(filename, search_term):
    """Search for term and show line numbers"""
    with open(filename, "r") as file:
        for line_num, line in enumerate(file, 1):
            if search_term.lower() in line.lower():
                print(f"Line {line_num}: {line.strip()}")

search_in_file("data.txt", "Python")
```

---

## File Operations

### Check if File Exists

```python
import os

if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File not found")
```

### Get File Information

```python
import os

if os.path.exists("file.txt"):
    size = os.path.getsize("file.txt")
    print(f"Size: {size} bytes")

    print(f"Is file: {os.path.isfile('file.txt')}")
    print(f"Is directory: {os.path.isdir('file.txt')}")
```

### Delete File

```python
import os

if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("File deleted")
```

### Copy File

```python
def copy_file(source, destination):
    with open(source, "r") as src:
        with open(destination, "w") as dst:
            dst.write(src.read())

copy_file("original.txt", "copy.txt")
```

### List Files in Directory

```python
import os

for filename in os.listdir("."):
    if os.path.isfile(filename):
        print(filename)
```

---

## Error Handling

Always handle file errors:

```python
try:
    with open("file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("❌ File not found!")
except PermissionError:
    print("❌ Permission denied!")
except Exception as e:
    print(f"❌ Error: {e}")
```

---

## Best Practices

### ✅ Do

1. **Always use `with` statement**
2. **Handle errors** with try-except
3. **Use appropriate mode** (r, w, a)
4. **Close files** (automatic with `with`)
5. **Use `strip()` to remove `\n`**

### ❌ Don't

```python
# ❌ BAD - Forget to close
file = open("file.txt", "r")
content = file.read()
# Forgot file.close()!

# ✅ GOOD - Automatic close
with open("file.txt", "r") as file:
    content = file.read()
```

---

## Quick Reference

### Reading

```python
# Read all
with open("file.txt", "r") as f:
    content = f.read()

# Read lines
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### Writing

```python
# Overwrite
with open("file.txt", "w") as f:
    f.write("Content")

# Append
with open("file.txt", "a") as f:
    f.write("More content")
```

### CSV

```python
import csv

# Write
with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### JSON

```python
import json

# Write
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read
with open("data.json", "r") as f:
    data = json.load(f)
```

---

## Summary

| Task        | Code           | Mode  |
| ----------- | -------------- | ----- |
| Read file   | `file.read()`  | `"r"` |
| Write file  | `file.write()` | `"w"` |
| Append file | `file.write()` | `"a"` |
| Read CSV    | `csv.reader()` | `"r"` |
| Write CSV   | `csv.writer()` | `"w"` |
| Read JSON   | `json.load()`  | `"r"` |
| Write JSON  | `json.dump()`  | `"w"` |

**Remember:**

- Use `with` statement always
- `"w"` overwrites, `"a"` appends
- Handle errors with try-except
- Use `strip()` to remove newlines

📁 [basics.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/file-handling/basics.py)  
📁 [practical.py](file:///Users/ragul/Documents/PERSONAL/python-starter-kit/starter_kit/file-handling/practical.py)
