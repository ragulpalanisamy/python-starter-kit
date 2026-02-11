# PyTest Basics

def add(a, b):
    return a + b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(10, 0) == 10

# To run this:
# 1. Install pytest: pip install pytest
# 2. Run command: pytest test_basics.py
