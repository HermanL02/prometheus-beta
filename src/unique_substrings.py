def find_unique_substrings(s: str) -> list[str]:
    """
    Find all unique substrings within the given string.
    
    Args:
        s (str): Input string to find unique substrings from
    
    Returns:
        list[str]: A list of unique substrings in the input string
    
    Examples:
        >>> find_unique_substrings("abcd")
        ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
        >>> find_unique_substrings("")
        []
        >>> find_unique_substrings("aaa")
        ['a', 'aa', 'aaa']
    """
    # Handle empty string case
    if not s:
        return []
    
    # Use a set to store unique substrings
    unique_substrings = set()
    
    # Generate all possible substrings
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            unique_substrings.add(s[start:end])
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_substrings))