# SOURCE: Leetcode
# https://leetcode.com/problems/maximum-subarray
# Solution: https://www.youtube.com/watch?v=5WZl3MMT0Eg (Neetcode)


# Time Complexity (TC): O(n): Traverse the array once and adjust the ptrs accordingly.
# Space Complexity (SC): O(1): Using constant extra memory
# Approach: Kadane's Algorithm: At every step check if curr_sum < 0 (negative) we will simply
# reset curr_sum because it is not contributing to finding the max sub array sum.
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
