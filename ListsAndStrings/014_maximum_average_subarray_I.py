# SOURCE: Leetcode
# https://leetcode.com/problems/maximum-average-subarray-i/description/


# Time Complexity (TC): O(n): Use sliding window approach and traverse the entire array
# Space Complexity (SC): O(1): constant memory is used
# Approach: Using sliding window approach, calculate the sum of first k elements
# start traversing the array and adjust the window by subtracting previous window starting element
# and adding upcoming element instead of calculating the sum of entire window. Compute max_sum at
# each iteration because if k is fixed then greater the max_sum, greater the average
def findMaxAverage(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Slide the window
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        if current_sum > max_sum:
            max_sum = current_sum

    # Return the average as a float
    return max_sum / float(k)
