# SOURCE: Leetcode
# https://leetcode.com/problems/height-checker/


# Solution # 1
# Time Complexity (TC): O(nlogn): Python sort function uses Tim sort - nlogn
# Space Complexity (SC): O(n): uses an extra array to keep the sorted list
# Approach: create a sorted version of input and then start comparing elements in each iteration
def height_checker_1(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    expected = sorted(heights)
    return sum(1 for i in range(len(heights)) if heights[i] != expected[i])
