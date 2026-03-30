# Simple unit tests for basic mathematical operations
import pytest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero not allowed")
    return a / b

def test_add_positive_numbers():
    result = add(2, 3)
    assert result == 5, f"Expected 5, got {result}"

def test_add_negative_numbers():
    result = add(-2, -3)
    assert result == -5, f"Expected -5, got {result}"

def test_divide_valid():
    result = divide(10, 2)
    assert result == 5, f"Expected 5, got {result}"

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
