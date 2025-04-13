# SOURCE: Leetcode
# https://leetcode.com/problems/assign-cookies
# Solution: https://www.youtube.com/watch?v=JW8fgvoxPTg (Neetcode)


# Solution # 1
# Time Complexity (TC): O(n log n+m log m): sorting takes O(n log n) time that's why we are considering this as well.
# Space Complexity (SC): O(1): No extra memory
# Approach: sort both lists because order is important. Take two ptrs and traverse both arrays.
# Once a cookie is used it cannot be used again or if it can't be used for one child then
# it can't be used for subsequent children either. So keep incrementing j irrespectively.
def find_content_children(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """

    g.sort()
    s.sort()
    i = j = 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            i += 1
        j += 1
    return i
