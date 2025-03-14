def int_to_roman(num: int) -> str:
    """
    Convert a non-negative integer to its Roman numeral representation.
    
    Args:
        num (int): An integer between 0 and 3999 (inclusive)
    
    Returns:
        str: Roman numeral representation of the input number
    
    Raises:
        ValueError: If the input is not between 0 and 3999
    """
    # Check input validity
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    
    if num < 0 or num > 3999:
        raise ValueError("Input must be between 0 and 3999")
    
    # Handle special case for 0
    if num == 0:
        return ""
    
    # Roman numeral conversion mapping
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
    
    # Build Roman numeral representation
    result = []
    for value, symbol in roman_map:
        while num >= value:
            result.append(symbol)
            num -= value
    
    return ''.join(result)