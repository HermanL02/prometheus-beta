import pytest
from src.unique_substrings import find_unique_substrings

def test_unique_substrings_basic():
    """Test basic substring generation"""
    result = find_unique_substrings("abcd")
    expected = ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
    assert sorted(result) == expected

def test_unique_substrings_with_repeats():
    """Test substring generation with repeated characters"""
    result = find_unique_substrings("aaa")
    expected = ['a', 'aa', 'aaa']
    assert sorted(result) == expected

def test_empty_string():
    """Test substring generation with empty string"""
    result = find_unique_substrings("")
    assert result == []

def test_single_character():
    """Test substring generation with single character"""
    result = find_unique_substrings("x")
    assert result == ['x']

def test_different_characters():
    """Test substring generation with diverse characters"""
    result = find_unique_substrings("hello")
    expected = ['e', 'el', 'ell', 'ello', 'h', 'he', 'hel', 'hell', 'hello', 'l', 'll', 'llo', 'lo', 'o']
    assert sorted(result) == expected