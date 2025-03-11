import pytest
from src.unique_substrings import get_unique_substrings

def test_unique_substrings_normal_case():
    """Test unique substrings for a typical string."""
    result = get_unique_substrings('abcb')
    expected = ['a', 'ab', 'abc', 'abcb', 'b', 'bc', 'bcb', 'c', 'cb']
    assert sorted(result) == sorted(expected)

def test_unique_substrings_empty_string():
    """Test unique substrings for an empty string."""
    result = get_unique_substrings('')
    assert result == []

def test_unique_substrings_single_char():
    """Test unique substrings for a single character string."""
    result = get_unique_substrings('a')
    assert result == ['a']

def test_unique_substrings_repeated_chars():
    """Test unique substrings with repeated characters."""
    result = get_unique_substrings('aaa')
    expected = ['a', 'aa', 'aaa']
    assert sorted(result) == sorted(expected)

def test_unique_substrings_all_unique_chars():
    """Test unique substrings with all unique characters."""
    result = get_unique_substrings('abc')
    expected = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert sorted(result) == sorted(expected)

def test_unique_substrings_long_string():
    """Test unique substrings for a longer string."""
    result = get_unique_substrings('hello')
    expected = ['h', 'he', 'hel', 'hell', 'hello', 
                'e', 'el', 'ell', 'ello', 
                'l', 'll', 'llo', 
                'lo', 
                'o']
    assert sorted(result) == sorted(expected)

def test_unique_substrings_comprehensive_case():
    """Test unique substrings with different input scenarios."""
    result = get_unique_substrings('abcd')
    expected = ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
    assert sorted(result) == expected