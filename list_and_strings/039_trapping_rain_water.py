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


# Two Pointers
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)
# Approach: Use two ptrs left and right -> move the smaller ptr because
# lower value determines the maximum amount of water stored -> keep track of both max values ->
# keep calculating units at each index
def trap_4(height):
    if not height:
        return 0

    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]
    res = 0
    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, height[l])
            res += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            res += right_max - height[r]
    return r


# Monotonic stack solution
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
# Approach: The stack here stores indices of bars in non-increasing height order.
# When we find a bar (height[i]) taller than the bar on top of the stack,
# it means we’ve found a right boundary for some trapped water.
# 	•	mid is the bar we just popped — it’s the bottom of the water container.
# 	•	The left boundary is now at stack[-1] (the new top of stack after popping mid).
# 	•	The right boundary is at i (current index).
def trap_5(height):
    if not height:
        return 0

    stack = []
    res = 0

    for i in range(len(height)):
        while stack and height[i] >= height[stack[-1]]:
            mid = height[stack.pop()]
            if stack:
                right = height[i]
                left = height[stack[-1]]
                h = min(right, left) - mid
                w = i - stack[-1] - 1
                # If you imagine the cross-section:
                # left boundary ... mid ... right boundary
                # The water in between these boundaries covers multiple columns (not just mid).
                # h * w
                # If you skipped width and only calculated “water at index i”, you’d miss all the water that’s over
                # multiple positions between boundaries.
                res += h * w
        stack.append(i)

    return res

# Todo - solve in future -> find in leetcode comments
# Got this follow up in the actual interview:
#
# Suppose a '0' in the input means that there is a leak at that position and the water can leak out. After the adjustment, that is, after the water levels have stabilized due to leaking, what is the answer?
#
# How do we change our approach/what would be out ideal answer for this scenario?
#
# Thanks in advance!
