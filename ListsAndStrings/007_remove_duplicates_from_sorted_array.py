# SOURCE: Leetcode
# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# Solution: https://www.youtube.com/watch?v=DEJAZBq0FDA (Neetcode)


# Solution # 1

# Time Complexity (TC): O(n): two pointer solution
# Space Complexity (SC): O(1): in-place swapping
# Approach:
def remove_duplicates(nums):
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l
