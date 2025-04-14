# SOURCE: Leetcode
# https://leetcode.com/problems/maximum-product-of-three-numbers
# Solution: Check comments section


# Solution # 1
# Time Complexity (TC):
# Space Complexity (SC): O(1): No extra memory
# Approach:
def maximum_product_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums.sort(reverse=True)
    p1 = nums[0] * nums[1] * nums[2]
    p2 = nums[-1] * nums[-2] * nums[0]
    return p1 if p1 >= p2 else p2
