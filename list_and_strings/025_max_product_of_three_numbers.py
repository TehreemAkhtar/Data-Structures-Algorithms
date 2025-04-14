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


# Solution # 2
# Time Complexity (TC): O(n): Just one loop
# Space Complexity (SC): O(1): No extra memory
# Approach: Iterate through the array once and compute max1, max2, max3, min1 and min2.
def maximum_product_2(nums):
    max1 = max2 = max3 = -float('inf')
    min1 = min2 = float('inf')

    for num in nums:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    p1 = max1 * max2 * max3
    p2 = max1 * min1 * min2
    return max(p1, p2)
