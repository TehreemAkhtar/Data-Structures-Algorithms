# Is Unique: Implement an algorithm to determine if a string has all unique characters.

# Assuming uniqueness is case-insensitive
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
# Uses sets
def is_unique_1(string):
    string = string.replace(" ", "")
    unique_chars = set()
    string = string.lower()
    for char in string:
        # Average TC O(1): sets use hashing
        if char in unique_chars:
            return False
        # Average TC O(1): sets use hashing
        unique_chars.add(char)
    return True


# Assuming uniqueness is case-insensitive
# Time Complexity (TC): O(n2)
# Space Complexity (SC): O(n)
# Uses strings
def is_unique_2(string):
    string = string.replace(" ", "")
    unique_chars = ''
    string = string.lower()
    for char in string:
        # Average TC O(n): searches linearly
        if char in unique_chars:
            return False
        # Average TC O(n): strings are immutable. Creates a new copy everytime
        unique_chars += char
    return True


# Assuming uniqueness is case-insensitive
# Time Complexity (TC): O(n2)
# Space Complexity (SC): O(1)
# without additional data structure
def is_unique_3(string):
    string = string.replace(" ", "")
    string = string.lower()
    length = len(string)
    for i in range(length):
        for j in range(i + 1, length):
            if string[i] == string[j]:
                return False
    return True


# Assuming uniqueness is case-insensitive
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
# Uses dicts i.e. classic hashmaps
def is_unique_4(string):
    unique_chars = {}
    string = string.replace(" ", "")
    string = string.lower()
    for char in string:
        if char in unique_chars:
            return False
        unique_chars[char] = True
    return True


# Assuming uniqueness is case-insensitive
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
def is_unique_5(string):
    string = string.replace(" ", "").lower()
    return len(string) == len(set(string))


# TODO: Implement Bit vector implementation