# SOURCE: Leetcode
# https://leetcode.com/problems/3sum/
# Solution: https://neetcode.io/solutions/3sum

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
