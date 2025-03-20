# SOURCE: Leetcode
# https://leetcode.com/problems/majority-element
# Solution: https://www.youtube.com/watch?v=7pnhv842keE (Neetcode)


# Solution # 1
# Time Complexity (TC): O(n2): uses brute-force approach
# Space Complexity (SC): O(1): using a constant amount of extra space
# Approach: Uses a brute force approach where we check all possible subarray sums
# and update pairs count
def majority_element_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maj_element = len(nums) // 2
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    for k, v in count.items():
        if v > maj_element:
            return k
