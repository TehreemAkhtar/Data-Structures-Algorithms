# SOURCE: Leetcode
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Solution: https://www.youtube.com/watch?v=ycAq8iqh0TI (Neetcode)


# Solution # 1

# Time Complexity (TC): O(n): two pointer solution
# Space Complexity (SC): O(1): in-place swapping
# Approach: Use two pointers l, r. Use r to count duplicates within the array. Use l to keep
# track of the output array length. Once r reaches the end of duplicate digits streak, run a loop at max
# 2 times to copy these elements and increment l ptr. Then move r ptr towards new streak of digits.
# This way at the end, l ptr will contain the required output with at max 2 duplicates.
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


# Solution # 2

# Time Complexity (TC): O(n): two pointer solution
# Space Complexity (SC): O(1): in-place swapping
# Approach: l ptr will keep track of the next valid element to be placed. It checks if an element is not the
# 3rd occurrence, it adds it to the valid part of the array
def remove_duplicates_2(nums):
    left = 2

    if len(nums) <= 2: return len(nums)

    for right in range(2, len(nums)):
        # If different: The current element is not a third duplicate. Place it at left, then increment left.
        # If same: skip to avoid 3rd occurrence and keep the ptr at the same position
        # until it can be replaced with a valid element.
        if nums[right] != nums[left - 2]:
            nums[left] = nums[right]
            left += 1

    return left
