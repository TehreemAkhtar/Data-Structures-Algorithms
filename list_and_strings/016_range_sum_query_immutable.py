# SOURCE: Leetcode
# https://leetcode.com/problems/range-sum-query-immutable
# Solution: https://www.youtube.com/watch?v=2pndAmo_sMA (Neetcode)


# Time Complexity (TC): O(n): one time prefix sum calculation within constructor
# Space Complexity (SC): O(n): An array to store prefix sum
# Approach: We will compute prefix sum once in the constructor so that everytime a query is made,
# we don't have to recalculate the sum. We can modify the prefix sum by subtracting the other sub array
# sum matching the query. This way every call to sumRange will be in constant time complexity
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = []
        curr_sum = 0
        for n in nums:
            curr_sum += n
            self.prefix_sum.append(curr_sum)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        right_sum = self.prefix_sum[right]
        left_sum = self.prefix_sum[left - 1] if left > 0 else 0
        return right_sum - left_sum
