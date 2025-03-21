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
# Time Complexity (TC): O(n): Traverses the array once by maintaining a prefix sum count in a hashmap
# Space Complexity (SC): O(n): Uses a hashmap to keep count of all subarray sums
# Approach: During each iteration, check the diff of curr_element - k, check if it is present in hashmap.
# This means we need (curr_element - k) subarray sum from hashmap to hold our condition true. We will also
# keep incrementing curr_sum count in the hashmap.
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
