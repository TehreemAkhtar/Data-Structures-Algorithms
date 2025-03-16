# SOURCE: Leetcode
# https://leetcode.com/problems/majority-element
# Solution: https://www.youtube.com/watch?v=7pnhv842keE (Neetcode)


def majorityElement(self, nums):
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