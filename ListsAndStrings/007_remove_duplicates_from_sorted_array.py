# SOURCE: Leetcode
# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# Solution: https://www.youtube.com/watch?v=DEJAZBq0FDA (Neetcode)


# Solution # 1

# Time Complexity (TC): O(n): two pointer solution
# Space Complexity (SC): O(1): in-place swapping
# Approach:
def remove_duplicates(nums):
    l, r = 0, 0
    while r < len(nums) - 1:
        if nums[r] != nums[r + 1]:
            nums[l + 1] = nums[r + 1]
            l += 1
        r += 1
    return l + 1
