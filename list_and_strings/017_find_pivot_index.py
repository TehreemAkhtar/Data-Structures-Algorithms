# SOURCE: Leetcode
# https://leetcode.com/problems/find-pivot-index/
# Solution: https://www.youtube.com/watch?v=u89i60lYx8U (Neetcode)

# Solution # 1
# Time Complexity (TC): O(n): use prefix sum approach
# Space Complexity (SC): O(n): using a list to store prefix sum
# Approach: Calculate prefix sum first. In second loop, check if left sum = right sum by
# excluding last index because the difference will always become equal at that point.
def pivot_index_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    prefix_sum = []
    total_sum = 0
    for n in nums:
        total_sum += n
        prefix_sum.append(total_sum)

    for i in range(len(nums)):
        left_sum = prefix_sum[i - 1] if i > 0 else 0
        right_sum = total_sum - prefix_sum[i] if i != len(nums) - 1 else 0
        if left_sum == right_sum:
            return i
    return -1


# Solution # 2
# Time Complexity (TC): O(n): use prefix sum approach
# Space Complexity (SC): O(1): no extra memory used except from a few variables
# Approach: Compute the total sum first. In each iteration, compute right and left sum and compare both.
# This way we don't need an extra list to maintain prefix sum as we can compute left sum in each iteration
def pivot_index_2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        left_sum += nums[i - 1] if i > 0 else 0
        right_sum = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            return i
    return -1


# Optimisation: Instead of having a conditional statement for left_sum in each iteration,
# simply compute right sum both and then do the comparison. Later on, update left_sum if needed
def pivot_index_2_optimised(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1
