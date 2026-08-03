# SOURCE: Leetcode
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# Solution: https://neetcode.io/solutions/largest-rectangle-in-histogram



# Time Complexity (TC): O(n): Traverse heights list once
# Space Complexity (SC): O(n): stack to store index and height

# Approach:
# Traverse each bar while maintaining a monotonic increasing stack of
# (start_index, height).
# If the current height is smaller than the stack's top height, the taller
# rectangle cannot extend any further to the right. Pop it and compute its
# area using:
#     height * (current_index - start_index)
# Keep the popped start_index so the current (shorter) height can start from
# that position, since it can extend over all previously popped taller bars.
# After processing all bars, compute the remaining rectangle areas in the stack
# using the array's length as the right boundary, and return the maximum area.
def largest_rectangle_area_1(heights):
    max_area = 0
    stack = []

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, (height * (i - index)))
            start = index

        stack.append((start, h))

    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    return max_area