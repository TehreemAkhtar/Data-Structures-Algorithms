# SOURCE: Leetcode
# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/


# Time Complexity (TC): O(n): Traverses the entire list and tries to typecast each element to int
# Space Complexity (SC): O(n): using an additional list to store each value to be compared
# Drawback: try-except is slower because catching an exception is expensive
def maximum_value_1(strs):
    """
    :type strs: List[str]
    :rtype: int
    """
    find_max = []
    for el in strs:
        try:
            find_max.append(int(el))
        except ValueError:
            find_max.append(len(el))
    return max(find_max)


# Time Complexity (TC): O(n): Traverses the entire list
# Space Complexity (SC): O(1): using a single var to track the max value encountered in each iteration
# Approach: In each iteration, check if the string consists of digits only (much faster than catching an exception)
# and perform operations accordingly
def maximum_value_2(strs):
    """
    :type strs: List[str]
    :rtype: int
    """
    max_value = 0
    for s in strs:
        curr = int(s) if s.isdigit() else len(s)
        max_value = max(max_value, curr)
    return max_value

