# SOURCE: Leetcode
# https://leetcode.com/problems/3sum/
# Solution: https://neetcode.io/solutions/3sum
from collections import defaultdict


# Solution # 1
# Time Complexity (TC): O(n2): Nested loop
# Space Complexity (SC): O(n2): worst case if result has all unique triplets,
# for i in range(n):
#     for j in range(i+1, n):
# This gives you:
# O(n^2) { pairs (i, j)}
# For each such pair, you’re checking if a third number (z = -x - y) exists in seen.
# If it does, you form a triplet and add it to result.
# So: The maximum number of valid triplets you could find using this method is bounded by O(n²) —
# the number of unique (i, j) pairs.

# Approach: Use nested loop -> outer loop sets the first number -> inner loop will behave like 2sum problem ->
# where we need to find z = -x - y (similar to 2sum hashmap solution)
def three_sum_1(nums):
    result = set()
    n = len(nums)

    for i in range(n):
        x = nums[i]
        seen = set()
        for j in range(i + 1, n):
            y = nums[j]
            z = -x - y
            if z in seen:
                triplet = tuple(sorted([x, y, z]))
                result.add(triplet)
            seen.add(y)

    return list(result)


# Solution # 2
# Time Complexity (TC): O(n2): Nested loop
# Space Complexity (SC): O(m): Where m is the number of triplets and n is the length of the given array.
# Approach: Use outer loop to set the first number and inner loop to reduce the problem to two pointer
# approach (imp to sort the array first) -> Use ptrs l and r to find all elements -> ignore duplicate numbers during
# the process as result set shouldn't contain duplicates.
def three_sum_2(nums):
    nums.sort()
    res = []

    for i in range(len(nums)):
        # Another optimisation
        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # skip duplicates
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif total < 0:
                l += 1
            else:
                r -= 1

    return res


# Solution # 3
# Time Complexity (TC): O(n2): Nested loop
# Space Complexity (SC): O(n): count dict size
# Approach:
#   1.  Sort the array
# 	2.	Track frequency of each number using count
# 	3.	Fix the first number nums[i] in the triplet
# 	4.	Iterate through all possible second numbers nums[j] after i
# 	5.	Use the formula target = -(nums[i] + nums[j])
# 	6.	If target is in the count and hasn’t already been used in this combination → it’s a valid triplet
def three_sum_3(nums):
    nums.sort()
    count = defaultdict(int)
    for num in nums:
        count[num] += 1

    res = []
    for i in range(len(nums)):
        count[nums[i]] -= 1
        if i and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums)):
            count[nums[j]] -= 1
            if j - 1 > i and nums[j] == nums[j - 1]:
                continue
            target = -(nums[i] + nums[j])
            if count[target] > 0:
                res.append([nums[i], nums[j], target])

        for j in range(i + 1, len(nums)):
            count[nums[j]] += 1
    return res
