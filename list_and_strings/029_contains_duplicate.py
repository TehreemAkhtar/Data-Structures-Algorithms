# SOURCE: Leetcode
# https://leetcode.com/problems/contains-duplicate
# Solution: https://neetcode.io/solutions/contains-duplicate


# Solution # 1
# Time Complexity (TC): O(n): as set traverses the whole array
# Space Complexity (SC): O(n): set is using additional memory
# Approach: As set contains unique elements, so we can compare len of both
# Drawbacks of this solution: this is not the best solution, suppose the duplicate numbers are in the init of
# the array and the array have an extreme large length, so you will have to create a extreme large set using
# more memory and time
def contains_duplicate_1(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) != len(set(nums))


# Solution # 2
# Time Complexity (TC): O(n log n): sort + traversing the array
# Space Complexity (SC): O(1): no extra memory
def contains_duplicate_2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    return any(nums[i] == nums[i + 1] for i in range(len(nums) - 1))


# First, nums[i] == nums[i + 1] for i in range(len(nums) - 1)
# ➔ This creates a generator that yields True if any two adjacent elements are equal.
# Then, any(...)
# ➔ any() will return True if at least one True appears in the generator.

# Solution # 3
# # Time Complexity (TC): O(n)
# # Space Complexity (SC): O(n): hashmap/set is using additional memory
def contains_duplicate_3(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
