import pytest
from src.integer_to_roman import int_to_roman

def test_int_to_roman_basic_conversions():
    """Test basic integer to Roman numeral conversions"""
    assert int_to_roman(1) == 'I'
    assert int_to_roman(4) == 'IV'
    assert int_to_roman(9) == 'IX'
    assert int_to_roman(14) == 'XIV'
    assert int_to_roman(49) == 'XLIX'
    assert int_to_roman(99) == 'XCIX'
    assert int_to_roman(500) == 'D'
    assert int_to_roman(3999) == 'MMMCMXCIX'

def test_int_to_roman_zero():
    """Test conversion of zero"""
    assert int_to_roman(0) == ''

def test_int_to_roman_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        int_to_roman(-1)
    
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        int_to_roman(4000)

def test_int_to_roman_type_error():
    """Test error handling for non-integer inputs"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_roman(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_roman("14")

def test_int_to_roman_comprehensive():
    """Comprehensive test of various integer to Roman numeral conversions"""
    test_cases = [
        (1, 'I'),
        (4, 'IV'),
        (9, 'IX'),
        (14, 'XIV'),
        (49, 'XLIX'),
        (99, 'XCIX'),
        (500, 'D'),
        (3999, 'MMMCMXCIX'),
        (2023, 'MMXXIII'),
        (1984, 'MCMLXXXIV')
    ]
    
    for num, expected in test_cases:
        assert int_to_roman(num) == expected