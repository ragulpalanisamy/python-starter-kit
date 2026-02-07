"""Example usage of the starter kit operations."""

import sys
from pathlib import Path

# Add parent directory to path so we can import starter_kit
sys.path.insert(0, str(Path(__file__).parent.parent))

from starter_kit import add, subtract, multiply, divide


def main():
    """Demonstrate basic operations."""
    print("🐍 Python Starter Kit - Operations Demo\n")
    
    # Addition
    print("➕ Addition:")
    print(f"  1 + 2 = {add(1, 2)}")
    print(f"  10 + 20 = {add(10, 20)}\n")
    
    # Subtraction
    print("➖ Subtraction:")
    print(f"  5 - 3 = {subtract(5, 3)}")
    print(f"  1 - 2 = {subtract(1, 2)}\n")
    
    # Multiplication
    print("✖️  Multiplication:")
    print(f"  3 × 4 = {multiply(3, 4)}")
    print(f"  5 × 5 = {multiply(5, 5)}\n")
    
    # Division
    print("➗ Division:")
    print(f"  10 ÷ 2 = {divide(10, 2)}")
    print(f"  7 ÷ 2 = {divide(7, 2)}\n")
    
    # Error handling
    print("⚠️  Error Handling:")
    try:
        result = divide(10, 0)
    except ValueError as e:
        print(f"  Caught error: {e}")


if __name__ == "__main__":
    main()
