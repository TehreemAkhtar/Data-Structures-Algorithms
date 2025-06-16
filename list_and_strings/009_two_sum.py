# SOURCE: Leetcode
# https://leetcode.com/problems/two-sum
# Solution: https://www.youtube.com/watch?v=KLlXCFG5TnA (Neetcode)
# https://neetcode.io/solutions/two-sum


# Solution # 1

# Time Complexity (TC): O(n): hashmap (dict) to track elements + indices
# Space Complexity (SC): O(n): using a hashmap which can store n-1 elements in worst case
# Approach: Use a hashmap to store traversed elements. In each iteration,
# check if the difference (target - current element) already exists in hashmap. If yes, return the index,
# else keep iterating.
def two_sum_1(nums, target):
    unique_elements = {}
    for i in range(len(nums)):
        element = target - nums[i]
        # dict.keys() return a dynamic view object, not a list. Checking 'element in unique_elements.keys()'
        # does not iterate through all keys - it directly checks the hashtable.
        # Membership checks are optimized via hashing.
        if element in unique_elements:
            return [i, unique_elements[element]]
        unique_elements[nums[i]] = i


def two_sum_1_refactored_version(nums, target):
    prev_map = dict()
    for i, n in enumerate(nums):
        diff = target - n
        # dict.keys() return a dynamic view object, not a list. Checking 'element in unique_elements.keys()'
        # does not iterate through all keys - it directly checks the hashtable.
        # Membership checks are optimized via hashing.
        if diff in prev_map:
            return [i, prev_map[diff]]
        prev_map[n] = i

# Follow-up: what if we have duplicate elements in array?
# 1. Either use set to remove duplicates
# 2. Use current solution but break the loop on first correct answer


# Follow-up: What if we have to print all possible pairs if array contains duplicates?
from collections import defaultdict

# Approach: Maintain a hashmap with key=num:value=[all indices]
# result = keep adding all pairs of indices to result
def all_two_sum_pairs(nums, target):
    seen = defaultdict(list)  # number -> list of positions
    result = []
    for i, num in enumerate(nums):
        complement = target - num
        for j in seen[complement]:
            result.append([j, i])
        seen[num].append(i)
    return result

# nums = [1,1,1,1], target = 2
# output = [[0,1], [0,2], [1,2], [0,3], [1,3], [2,3]]
