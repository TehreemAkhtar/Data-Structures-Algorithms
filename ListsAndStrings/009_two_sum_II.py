# SOURCE: Leetcode
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Solution: https://www.youtube.com/watch?v=cQ1Oz4ckceM (Neetcode)

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
