# SOURCE: Leetcode
# https://leetcode.com/problems/maximum-product-subarray
# Solution: https://www.youtube.com/watch?v=lXVy6YWFcRM&t=19s (Neetcode)


# Solution # 1
# Time Complexity (TC): O(n):
# Space Complexity (SC): O(1): No extra memory
# Approach: Not actually Kadane algo but a modification of Kadane. Keep track of min and max product
# in each iteration because we have -ve values and so two -ve's can form a +v2. Keep updating res with the
# max value and return it in the end.
# Further explanation:
# Same as kadane’s algorithm for maximum subarray, where we keep track of max subarray ending at ith index.
# For this problem since two negatives multiplied together give a positive,
# we need to keep track of the min subarray ending at ith index AND max subarray ending at ith index.
# Then for i+1 position, if it’s a negative value, then the max product subarray ending at i+1 position is
# that value * min subarray ending at ith position (if it’s negative value)
# Dealing with 0s as elements, the zero resets our min and max subarray ending at 0 element’s index.
# So both min and max become 1 after encountering 0
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
