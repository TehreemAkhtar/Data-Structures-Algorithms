# SOURCE: Leetcode
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Solution: https://www.youtube.com/watch?v=cQ1Oz4ckceM (Neetcode)


# Solution # 1

# Time Complexity (TC): O(n log n): traversing the entire list and calling binary search (log n)
# in each iteration to find the diff
# Space Complexity (SC): O(1): we're not storing anything anywhere
# Approach:
def two_sum(numbers, target):
    length = len(numbers)
    for i, n in enumerate(numbers):
        diff = target - n
        res = binary_search(i + 1, length - 1, numbers, diff)
        if res != -1:
            return [i + 1, res + 1]


def binary_search(l, r, nums, target):
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1
