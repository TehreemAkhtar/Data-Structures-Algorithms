# SOURCE: Leetcode
# https://leetcode.com/problems/sort-colors/
# Solution: https://www.youtube.com/watch?v=4xbWSRZHqac (Neetcode)
from heapq import heappop


# Solution # 1
# Time Complexity (TC): O(n): Use three pointers to sort the array in one pass
# Space Complexity (SC): O(1): Just uses three variables
# Approach: Uses Dutch National Flag (DNF) algorithm to sort the limited numbers in array in one pass
# by using 1 left ptr, 1 right ptr and i ptr to traverse the array
# left ptr sorts 0's in the array
# right ptr sort 2's in the array
# We skip 1's because they'll stay in middle
# The DNF algorithm is a simplified, specialized version of three-way partitioning (used in Quick Sort).
# Both use pointers to group elements efficiently in linear time, but DNF is tailored for three fixed distinct values,
# while Quick Sort is a full sorting algorithm.
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
            heappop()

# Approach 2 can be implemented using counting sort but that would require two passes
# and the solution requires one pass only
