# SOURCE: Leetcode
# https://leetcode.com/problems/container-with-most-water/description/
# Solution: https://neetcode.io/solutions/container-with-most-water

# Solution # 1
# Time Complexity (TC): O(n): two ptrs to traverse the heights once
# Space Complexity (SC): O(1)
# Approach: use two ptrs l and r -> move the pointer pointing to a small height i.e. Always
# move the pointer that points to the lower line.
def max_area_1(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        max_area = max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area
