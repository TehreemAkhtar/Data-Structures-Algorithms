# SOURCE: Leetcode
# https://leetcode.com/problems/third-maximum-number
# Solution: https://leetcode.com/problems/third-maximum-number/editorial/

# Solution # 1
# Time Complexity (TC): O(n): Use set to remove duplicates and max values one by one
# Space Complexity (SC): O(1): No extra space used
# Approach: Create a set to remove duplicates -> remove first 3 max values -> if only 1 exists then
# it'll be caught by exception
def third_max_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = list(set(nums))

    first_max = max(nums)
    nums.remove(first_max)
    try:
        second_max = max(nums)
        nums.remove(second_max)

        third_max = max(nums)
        nums.remove(third_max)
    except ValueError:
        return first_max
    return third_max

# Rest of the solutions can be read from LC editorial
