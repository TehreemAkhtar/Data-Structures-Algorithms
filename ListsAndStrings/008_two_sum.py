# SOURCE: Leetcode
# https://leetcode.com/problems/two-sum
# Solution: https://www.youtube.com/watch?v=KLlXCFG5TnA (Neetcode)


# Solution # 1

# Time Complexity (TC): O(n): hashmap (dict) to track elements + indices
# Space Complexity (SC): O(n): using a hashmap which can store n-1 elements in worst case
# Approach:
def two_sum_1(nums, target):
    unique_elements = dict()
    for i in range(len(nums)):
        element = target - nums[i]
        # dict.keys() return a dynamic view object, not a list. Checking 'element in unique_elements.keys()'
        # does not iterate through all keys - it directly checks the hashtable.
        # Membership checks are optimized via hashing.
        if element in unique_elements.keys():
            return [i, unique_elements[element]]
        unique_elements[nums[i]] = i
