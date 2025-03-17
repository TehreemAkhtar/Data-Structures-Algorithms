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
