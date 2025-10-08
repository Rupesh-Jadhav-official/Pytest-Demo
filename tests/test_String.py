# This file contains unit tests for string manipulation functions.

def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

def test_reverse_string():
    result = reverse_string("hello")
    assert result == "olleh", f"Expected 'olleh', got {result}"

def test_capitalize_string():
    result = capitalize_string("python")
    assert result == "Python", f"Expected 'Python', got {result}"
