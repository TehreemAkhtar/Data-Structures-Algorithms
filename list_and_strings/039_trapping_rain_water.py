# SOURCE: Leetcode
# https://leetcode.com/problems/trapping-rain-water/description/
# Solution: https://neetcode.io/solutions/trapping-rain-water


# Brute force solution
# Time Complexity (TC): O(n2): the bottleneck is call to max function with sliced array
# Space Complexity (SC): O(1):
# Approach: In each iteration -> compute left max and right max -> use it in the formula
def trap_1(height):
    n = len(height)
    units = 0
    for i in range(1, n - 1):
        max_l = max(height[:i])
        max_r = max(height[i + 1:])
        water = min(max_l, max_r) - height[i]
        if water > 0:
            units += water
    return units


# Brute force solution
# Time Complexity (TC): O(n2): the bottleneck is call to max function with sliced array
# Space Complexity (SC): O(1):
# Approach: In each iteration -> compute left max and right max -> use it in the formula
def trap_2(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
        return 0
    n = len(height)
    res = 0

    for i in range(n):
        left_max = right_max = height[i]

        for j in range(i):
            left_max = max(left_max, height[j])
        for j in range(i + 1, n):
            right_max = max(right_max, height[j])

        res += min(left_max, right_max) - height[i]
    return res


# Prefix & Suffix Arrays
# Time Complexity (TC): O(n): precompute left and right max for each index
# Space Complexity (SC): O(n): left and right max arrays
# Approach: Iterate through height array -> precompute left and right max -> in last iteration, calculate total units
def trap_3(height):
    n = len(height)
    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    res = 0
    for i in range(n):
        res += min(left_max[i], right_max[i]) - height[i]
    return res
