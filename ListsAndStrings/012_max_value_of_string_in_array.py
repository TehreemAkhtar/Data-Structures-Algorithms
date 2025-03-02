# SOURCE: Leetcode
# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/


# Time Complexity (TC): O(n): Traverses the entire list and tries to typecast each element to int
# Space Complexity (SC): O(n): using an additional list to store each value to be compared
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
