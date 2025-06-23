# SOURCE: Leetcode
# https://leetcode.com/problems/valid-palindrome/description/
# Solution: https://neetcode.io/solutions/valid-palindrome (Neetcode)


# Solution # 1
# Time Complexity (TC): O(n): a full iteration
# Space Complexity (SC): O(n): using a new str
# Approach: create a new string -> reverse it -> compare with original
def is_palindrome_1(s):
    sanitized_s = ''.join([c.lower() for c in s if c.isalnum()])
    return sanitized_s == sanitized_s[::-1]


# Solution # 2
# Time Complexity (TC): O(n): a full iteration
# Space Complexity (SC): O(n): using a new str list
# Approach: create a new list -> use two ptrs l and r and compare start and end of string
def is_palindrome_2(s):
    sanitized_s = [c.lower() for c in s if c.isalnum()]
    l, r = 0, len(sanitized_s) - 1

    while l < r:
        if sanitized_s[l] != sanitized_s[r]:
            return False
        l += 1
        r -= 1
    return True


# Solution # 2
# Time Complexity (TC): O(n): a full iteration
# Space Complexity (SC): O(1): no extra memory
# Approach: create a new list -> use two ptrs l and r and compare start and end of string
def is_palindrome_2_optimised(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alpha_num(s[l]):
            l += 1
        while r > l and not alpha_num(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


def alpha_num(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
