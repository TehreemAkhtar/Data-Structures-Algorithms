# SOURCE: Leetcode
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


# Time Complexity (TC): O(n): Use kadane algo with slight modification
# Space Complexity (SC): O(1): constant memory is used
# Approach: Maintain two sums prev and curr. Prev_sum will sum of prev sub array of 1 i.e.
# before encountering a zero and curr_sum will hold current count of ones i.e. once a 0 is
# encountered. At each step we will keep checking is prev+curr sum is greater than max_sum.
def longest_subarray_1(nums):
    max_sum = curr_sum = prev_sum = 0
    for num in nums:
        if num == 0:
            prev_sum = curr_sum
            curr_sum = 0
        else:
            curr_sum += 1
        max_sum = max(max_sum, prev_sum + curr_sum)
    return max_sum - 1 if max_sum == len(nums) else max_sum


# Time Complexity (TC): O(n): Use sliding window approach while only traversing the array once
# Space Complexity (SC): O(1): constant memory is used
# Approach: Maintain a valid window of elements with at most 1 zero. If the window contains > 1 zeros, then
# move the start ptr to the left until the window becomes valid again and has at most 1 zero. Keep checking the
# length of the valid window in each iteration
def longest_subarray_2(nums):
    zero_count = longest_window = start = 0

    for i, n in enumerate(nums):
        zero_count += (n == 0)

        while zero_count > 1:
            zero_count -= (nums[start] == 0)
            start += 1
        longest_window = max(longest_window, i - start)
    return longest_window
