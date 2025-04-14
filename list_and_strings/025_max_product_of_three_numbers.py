# SOURCE: Leetcode
# https://leetcode.com/problems/maximum-product-of-three-numbers
# Solution: Check comments section


# Solution # 1
# Time Complexity (TC): n Log n: Because we are sorting
# Space Complexity (SC): O(1): No extra memory
# Approach: The max product can either be the product of first 3 max +ve or -ve numbers. BUT
# if the array contains both +ve and -ve then it can be product of last 2 (smallest) -ve numbers and max +ve num
def maximum_product_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums.sort(reverse=True)
    p1 = nums[0] * nums[1] * nums[2]
    p2 = nums[-1] * nums[-2] * nums[0]
    return p1 if p1 >= p2 else p2
