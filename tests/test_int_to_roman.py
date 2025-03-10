import pytest
from src.int_to_roman import int_to_roman

def test_zero():
    """Test conversion of 0 to an empty string."""
    assert int_to_roman(0) == ""

def test_single_digit_numbers():
    """Test conversion of single-digit numbers."""
    assert int_to_roman(1) == "I"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(5) == "V"
    assert int_to_roman(9) == "IX"

def test_double_digit_numbers():
    """Test conversion of double-digit numbers."""
    assert int_to_roman(10) == "X"
    assert int_to_roman(14) == "XIV"
    assert int_to_roman(40) == "XL"
    assert int_to_roman(49) == "XLIX"
    assert int_to_roman(99) == "XCIX"

def test_triple_digit_numbers():
    """Test conversion of triple-digit numbers."""
    assert int_to_roman(100) == "C"
    assert int_to_roman(400) == "CD"
    assert int_to_roman(500) == "D"
    assert int_to_roman(900) == "CM"

def test_large_numbers():
    """Test conversion of large numbers."""
    assert int_to_roman(1984) == "MCMLXXXIV"
    assert int_to_roman(3999) == "MMMCMXCIX"

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        int_to_roman(-1)
    
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        int_to_roman(4000)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_roman("123")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_roman(3.14)