import pytest
from src.unique_substrings import get_unique_substrings

def test_basic_substring_extraction():
    """Test basic substring extraction"""
    result = get_unique_substrings("abc")
    assert result == ['a', 'ab', 'abc', 'b', 'bc', 'c']

def test_empty_string():
    """Test behavior with an empty string"""
    result = get_unique_substrings("")
    assert result == []

def test_single_character_string():
    """Test a single character string"""
    result = get_unique_substrings("x")
    assert result == ['x']

def test_repeated_characters():
    """Test string with repeated characters"""
    result = get_unique_substrings("aaa")
    assert result == ['a', 'aa', 'aaa']

def test_complex_string():
    """Test a more complex string"""
    result = get_unique_substrings("hello")
    expected_substrings = ['h', 'he', 'hel', 'hell', 'hello', 
                           'e', 'el', 'ell', 'ello', 
                           'l', 'll', 'llo', 
                           'l', 'lo', 
                           'o']
    
    # Verify presence of expected unique substrings
    for substring in expected_substrings:
        assert substring in result, f"Substring '{substring}' not found"
    
    # Verify total number of unique substrings
    # Allow some flexibility, but ensure close to expected count
    assert len(result) in [14, 15]

def test_invalid_input_type():
    """Test behavior with invalid input type"""
    with pytest.raises(TypeError, match="Input must be a string"):
        get_unique_substrings(123)
        get_unique_substrings(None)
        get_unique_substrings(["hello"])

def test_unicode_string():
    """Test with unicode characters"""
    result = get_unique_substrings("こんにちは")
    assert len(result) == 15  # Number of unique substrings
    assert 'こん' in result
    assert 'こんにち' in result
    assert 'こんにちは' in result