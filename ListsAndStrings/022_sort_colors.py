# SOURCE: Leetcode
# https://leetcode.com/problems/sort-colors/
# Solution: https://www.youtube.com/watch?v=4xbWSRZHqac (Neetcode)


# Solution # 1
# Time Complexity (TC): O(n): Python sort function uses Tim sort - nlogn
# Space Complexity (SC): O(1): uses an extra array to keep the sorted list
# Approach: create a sorted version of input and then start comparing elements in each iteration
def sort_colors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    l, r = 0, len(nums) - 1
    i = 0

    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        else:
            i += 1
