# SOURCE: Leetcode
# https://leetcode.com/problems/subarray-sum-equals-k
# Solution: https://www.youtube.com/watch?v=fFVZt-6sgyo (Neetcode)


# Solution # 1
# Time Complexity (TC): O(n2): uses brute-force approach
# Space Complexity (SC): O(1): using a constant amount of extra space
# Approach: Uses a brute force approach where we check all possible subarray sums
# and update pairs count
def subarray_sum_1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    pairs = 0
    for i in range(len(nums)):
        sum_ = 0
        for j in range(i, len(nums)):
            sum_ += nums[j]
            if sum_ == k:
                pairs += 1
    return pairs


# Solution # 2
# Time Complexity (TC): O(n): use prefix sum approach
# Space Complexity (SC): O(1): no extra memory used except from a few variables
# Approach: Compute the total sum first. In each iteration, compute right and left sum and compare both.
# This way we don't need an extra list to maintain prefix sum as we can compute left sum in each iteration
def subarray_sum_2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    pairs = curr_sum = 0
    prefix_sum_count = {0: 1}

    for n in nums:
        curr_sum += n
        diff = curr_sum - k
        pairs += prefix_sum_count.get(diff, 0)
        prefix_sum_count[curr_sum] = 1 + prefix_sum_count.get(curr_sum, 0)
    return pairs
