def get_unique_substrings(input_string):
    """
    Generate all unique substrings of the given input string.
    
    Args:
        input_string (str): The input string to extract unique substrings from.
    
    Returns:
        list: A list of unique substrings sorted in order of appearance.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> get_unique_substrings("abc")
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
        >>> get_unique_substrings("")
        []
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If the input is empty, return an empty list
    if not input_string:
        return []
    
    # Use a set to track unique substrings, but maintain order of appearance
    unique_substrings = []
    seen = set()
    
    # Generate all possible substrings
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            substring = input_string[start:end]
            if substring not in seen:
                unique_substrings.append(substring)
                seen.add(substring)
    
    return unique_substrings