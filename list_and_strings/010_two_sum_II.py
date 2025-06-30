# SOURCE: Leetcode
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Solution: https://www.youtube.com/watch?v=cQ1Oz4ckceM (Neetcode)


# Solution # 1

# Time Complexity (TC): O(n log n): traversing the entire list and calling binary search (log n)
# in each iteration to find the diff
# Space Complexity (SC): O(1): we're not storing anything anywhere
# Approach: Traverse the entire list. In each iteration i, apply binary search on the sub-array (i+1 -> len(arr)-1)
# and check if the diff exists.
def two_sum_1(numbers, target):
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


# Solution # 2

# Time Complexity (TC): O(n): traversing the entire list using 2 ptrs and check the sum of nums in each iteration
# Space Complexity (SC): O(1): we're not storing anything anywhere
# Approach: Use two pointers l and r, in each iteration check the following
# if sum(l+r) == target
# if sum(l+r) > target: which means if we move l pointer inwards,
# the sum would increase because the list is sorted. Instead, we will move r pointers inwards.
# if sum(l+r) < target, move the l ptr, so the sum can increase
def two_sum_2(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        _sum = numbers[l] + numbers[r]
        if _sum == target:
            return [l + 1, r + 1]
        if _sum > target:
            r -= 1
        else:
            l += 1
