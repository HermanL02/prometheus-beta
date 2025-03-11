def int_to_roman(num):
    """
    Convert an integer to its Roman numeral representation.
    
    Args:
        num (int): Non-negative integer between 0 and 3999.
    
    Returns:
        str: Roman numeral representation of the input number.
    
    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is outside the valid range (0-3999).
    """
    # Input validation
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    
    if num < 0 or num > 3999:
        raise ValueError("Input must be between 0 and 3999")
    
    # Special case for zero
    if num == 0:
        return ""
    
    # Roman numeral symbols from largest to smallest
    roman_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    # Build Roman numeral string
    result = []
    for value, symbol in roman_map:
        while num >= value:
            result.append(symbol)
            num -= value
    
    return ''.join(result)