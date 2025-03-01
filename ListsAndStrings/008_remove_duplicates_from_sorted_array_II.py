# SOURCE: Leetcode
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Solution: https://www.youtube.com/watch?v=ycAq8iqh0TI (Neetcode)


# Solution # 1

# Time Complexity (TC): O(n): two pointer solution
# Space Complexity (SC): O(1): in-place swapping
# Approach:
def remove_duplicates_1(nums):
    l, r = 0, 0
    while r < len(nums):
        count = 1
        while r + 1 < len(nums) and nums[r] == nums[r + 1]:
            count += 1
            r += 1
        for _ in range(min(2, count)):
            nums[l] = nums[r]
            l += 1
        r += 1
    return l
