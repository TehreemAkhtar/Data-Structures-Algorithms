# Is Unique: Implement an algorithm to determine if a string has all unique characters.

# Assuming uniqueness is case-insensitive
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
def is_unique_1(string):
    unique_chars = set()
    string = string.lower()
    for char in string:
        # Average TC O(1): sets use hashing
        if char in unique_chars:
            return False
        # Average TC O(1): sets use hashing
        unique_chars.add(char)
    return True
