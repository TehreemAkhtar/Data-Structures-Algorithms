# SOURCE: Leetcode
# https://leetcode.com/problems/maximum-product-subarray
# Solution: https://www.youtube.com/watch?v=lXVy6YWFcRM&t=19s (Neetcode)


# Solution # 1
# Time Complexity (TC): O(n):
# Space Complexity (SC): O(1): No extra memory
# Approach: Not actually Kadane algo but a modification of Kadane
def max_product(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    res = max(nums)
    curr_min = curr_max = 1

    for n in nums:
        curr_max, curr_min = max(n * curr_max, n * curr_min, n), min(n * curr_max, n * curr_min, n)
        res = max(curr_max, curr_min, res)
    return res
