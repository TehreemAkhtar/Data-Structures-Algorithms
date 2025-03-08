# SOURCE: Leetcode
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


# Time Complexity (TC): O(n): Use sliding window approach and traverse the entire array
# Space Complexity (SC): O(1): constant memory is used
# Approach:
def longest_subarray(nums, k):
    max_sum = curr_sum = prev_sum = 0
    for num in nums:
        if num == 0:
            prev_sum = curr_sum
            curr_sum = 0
        else:
            curr_sum += 1
        max_sum = max(max_sum, prev_sum + curr_sum)
    return max_sum - 1 if max_sum == len(nums) else max_sum
