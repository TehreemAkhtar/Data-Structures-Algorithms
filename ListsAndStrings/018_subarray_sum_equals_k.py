# SOURCE: Leetcode
# https://leetcode.com/problems/subarray-sum-equals-k
# Solution: https://www.youtube.com/watch?v=fFVZt-6sgyo (Neetcode)


# Brute force
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
