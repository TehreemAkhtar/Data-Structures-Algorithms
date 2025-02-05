# SOURCE: Leetcode
# https://leetcode.com/problems/reverse-string/
# Solution: https://www.youtube.com/watch?v=_d0T_2Lk2qA (Neetcode)


# Solution # 1

# Time Complexity (TC): O(n): two pointer solution
# Space Complexity (SC): O(1): in-place swapping
# Approach: Use two pointers i and j -> swap their positions
def reverse_string_1(s):
    j = len(s) - 1
    for i in range(len(s) // 2):
        s[i], s[j - i] = s[j - i], s[i]
    return s
