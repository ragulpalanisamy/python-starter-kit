# 🐍 Python Architecture

> **How Python runs your code** - explained visually

---

## 📚 Two Types of Languages

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  HLL (High-Level Language)        LLL (Low-Level Language) │
│  ✍️  Human-Readable                🤖 Machine-Readable      │
│                                                             │
│  Example: Python, Java            Example: 0101010101      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 How Code Runs

### Traditional Languages (C, C++)

```
📝 Source Code  →  🔨 Compiler  →  ⚙️  Machine Code  →  ✅ Run
   (You write)      (Translates)     (Computer runs)
```

### Python's Way

```
📝 Source Code  →  🔨 Compiler  →  📦 Bytecode  →  🐍 PVM  →  ⚙️  Machine Code  →  ✅ Run
   (You write)      (Translates)    (.pyc file)   (Interprets)  (Computer runs)
```

---

## 🎯 Python Execution in 2 Phases

### Example: `print("Hello")`

```
┌──────────────────────────────────────────────────────────────┐
│                    ⏱️  COMPILE TIME                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   print("Hello")  →  Compiler  →  Bytecode (.pyc)          │
│                                                              │
│   ✓ Check syntax                                            │
│   ✓ Convert to intermediate code                            │
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                    🚀 RUNTIME                                │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   Bytecode  →  PVM  →  Machine Code  →  Output: Hello      │
│                                                              │
│   ✓ Load bytecode                                           │
│   ✓ Interpret line-by-line                                  │
│   ✓ Execute on CPU                                          │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 🖼️ Visual Architecture

![Python Architecture Diagram](architecture.png)

### Legend

| Symbol | Meaning                             |
| ------ | ----------------------------------- |
| 📝     | Your Python code (.py file)         |
| 🔨     | Compiler (converts to bytecode)     |
| 📦     | Bytecode (.pyc - intermediate code) |
| 🐍     | PVM (Python Virtual Machine)        |
| ⚙️     | Machine code (runs on CPU)          |

---

---

## ⚡ Modes of Execution

Python allows you to run code in two primary ways:

### 1. Interactive Mode (REPL)

- **What it is:** A "Read-Eval-Print Loop" where you type code and see results immediately.
- **How to use:** Type `python` in your terminal.
- **Best for:** Testing small snippets, debugging, and learning.
- **Example:**
  ```python
  >>> x = 10
  >>> print(x * 2)
  20
  ```

### 2. Script Mode

- **What it is:** Writing code in a `.py` file and running the entire file at once.
- **How to use:** `python filename.py`
- **Best for:** Building applications, automation scripts, and larger projects.

**Key Benefit:** Python bytecode runs on any OS/Processor with Python installed!

---

_Updated: Feb 2026_
