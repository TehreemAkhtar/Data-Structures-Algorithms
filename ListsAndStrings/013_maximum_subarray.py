# SOURCE: Leetcode
# https://leetcode.com/problems/maximum-subarray
# Solution: https://www.youtube.com/watch?v=5WZl3MMT0Eg (Neetcode)


# Time Complexity (TC): O(n): Traverses the entire list and tries to typecast each element to int
# Space Complexity (SC): O(1): using an additional list to store each value to be compared
# Drawback: try-except is slower because catching an exception is expensive
def max_sub_array(nums):
    """
    :type strs: List[str]
    :rtype: int
    """
    max_sub = nums[0]
    curr_sum = 0

    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n
        max_sub = max(max_sub, curr_sum)
    return max_sub
