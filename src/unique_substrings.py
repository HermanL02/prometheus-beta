def get_unique_substrings(s: str) -> list[str]:
    """
    Generate all unique substrings within the given string.
    
    Args:
        s (str): Input string to extract unique substrings from.
    
    Returns:
        list[str]: A list of unique substrings in the input string.
    
    Examples:
        >>> get_unique_substrings('abcb')
        ['a', 'ab', 'abc', 'abcb', 'b', 'bc', 'bcb', 'c', 'cb']
        >>> get_unique_substrings('')
        []
    """
    # Handle empty string case
    if not s:
        return []
    
    # Use a set to ensure uniqueness
    unique_substrings = set()
    
    # Generate all possible substrings
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            unique_substrings.add(s[start:end])
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_substrings))