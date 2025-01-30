# SOURCE: Leetcode
# https://leetcode.com/problems/binary-search/
# Solution: https://www.youtube.com/watch?v=s4DPM8ct1pI (Neetcode)


# Solution # 1

# Time Complexity (TC): O(log n): binary search
# Space Complexity (SC): O(1)
# Approach: Use Binary Search
def search_1(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1
