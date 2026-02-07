"""Unit tests for operations module."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path so we can import starter_kit
sys.path.insert(0, str(Path(__file__).parent.parent))

from starter_kit.operations import add, subtract, multiply, divide


class TestAddition:
    """Test cases for add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(1, 2) == 3
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-1, -2) == -3
        assert add(-5, 5) == 0
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(1.5, 2.5) == 4.0
        assert add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtraction:
    """Test cases for subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 5) == 5
    
    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative."""
        assert subtract(1, 2) == -1
        assert subtract(0, 5) == -5


class TestMultiplication:
    """Test cases for multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(3, 4) == 12
        assert multiply(5, 5) == 25
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6


class TestDivision:
    """Test cases for divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5.0
        assert divide(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
    def test_divide_negative_numbers(self):
        """Test dividing with negative numbers."""
        assert divide(-10, 2) == -5.0
        assert divide(10, -2) == -5.0
        assert divide(-10, -2) == 5.0
