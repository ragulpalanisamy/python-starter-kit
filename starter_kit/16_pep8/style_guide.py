"""
PEP 8 Style Guide Example

This script demonstrates PEP 8 recommendations for:
1. Indentation
2. Naming conventions
3. Spacing around operators
4. Docstrings
"""

# Standard library imports first
import os
import sys

# Constants (UPPER_CASE)
MAX_RETRIES = 3


class UserProfile:
    """
    PascalCase for class names.
    Docstrings explain the purpose of the class.
    """

    def __init__(self, user_id: int, user_name: str):
        # snake_case for variables
        self.user_id = user_id
        self.user_name = user_name

    def display_info(self):
        """Docstrings for methods."""
        print(f"User [{self.user_id}]: {self.user_name}")


def calculate_total(price: float, quantity: int) -> float:
    """
    Calculate the total price with a fixed tax.
    
    snake_case for function names.
    Spaces around operators (price * quantity).
    """
    tax_rate = 0.08  # snake_case for local variables
    subtotal = price * quantity
    total = subtotal * (1 + tax_rate)
    return round(total, 2)


def main():
    # 4 spaces for indentation
    users = [
        UserProfile(1, "Alice"),
        UserProfile(2, "Bob"),
    ]

    for user in users:
        user.display_info()

    total = calculate_total(19.99, 3)
    print(f"\nTotal Price (inc. tax): ${total}")


if __name__ == "__main__":
    main()
