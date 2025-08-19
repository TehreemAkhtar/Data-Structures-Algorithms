# SOURCE: Leetcode
# https://leetcode.com/problems/valid-parentheses/
# Solution: https://neetcode.io/solutions/valid-parentheses


# Brute force solution
# Time Complexity (TC): O(n2): the 'in' check costs a full scan -> replace also scans the entire list
# -> creates a new string
# Space Complexity (SC): O(n): string s to store updated string
# Approach: Keep cancelling out/removing bracket pairs from strings -> if end up with empty string
# -> valid pair -> else invalid pair
def is_valid_1(s):
    """
    :type s: str
    :rtype: bool
    """
    # So worst case: it checks all three: That’s 3 scans of the string → 3 × O(n) = O(n).
    while '()' in s or '{}' in s or '[]' in s:
        # replace also scans the whole string and builds a new string.
        s = s.replace('()', '')
        s = s.replace('{}', '')
        s = s.replace('[]', '')
    return s == ''


# Stack solution
# Time Complexity (TC): O(n): a single iteration
# Space Complexity (SC): O(n): string s to store updated string
# Approach: Iterate through string -> for any opening bracket -> push to stack ->
# closing bracket -> match it with stack top
def is_valid_2(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 != 0:
        return False
    stack = []
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in bracket_mapping:
            if stack and stack[-1] == bracket_mapping[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return not stack
