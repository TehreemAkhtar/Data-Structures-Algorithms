# SOURCE: Leetcode
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


# Time Complexity (TC): O(n): Use kadane algo with slight modification
# Space Complexity (SC): O(1): constant memory is used
# Approach: Maintain two sums prev and curr. Prev_sum will sum of prev sub array of 1 i.e.
# before encountering a zero and curr_sum will hold current count of ones i.e. once a 0 is
# encountered. At each step we will keep checking is prev+curr sum is greater than max_sum.
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
