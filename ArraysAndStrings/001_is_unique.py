# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Assuming uniqueness is case-insensitive
def is_unique_1(string):
    unique_chars = set()
    string = string.lower()
    for char in string:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    return True
