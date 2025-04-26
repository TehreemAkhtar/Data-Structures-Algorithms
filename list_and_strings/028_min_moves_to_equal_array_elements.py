# SOURCE: Leetcode
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/


# Solution # 1
# Time Complexity (TC): O(n):
# Space Complexity (SC): O(1): No extra memory
# Approach: As per the question: In each move, we increase n−1 elements by 1.
# But we found it’s equivalent to decreasing 1 element by 1 instead
# (because if you increase all others by 1, it’s like pulling one down relatively).
# So, instead of:
# [1,2,3] -> [2,3,3] -> [3,3,4] -> [4,4,4] = 3 moves
#
# We do:
# [1,2,3] -> [1,2,2] -> [1,1,2] -> [1,1,1] = 3 moves
# We need to find out how much subtracts should happen, and it always will be related to the minimum number. So, in our case, if it's 1 (one), then we need to find out how much different to subtract. So:
#
# 3 - 1 = 2
# 2 - 1 = 1
# 1 - 1 = 0
# Now we sum the difference: 2 + 1 + 0 = 3, so we got here! 3 moves!
def min_moves_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    min_ = min(nums)
    count = 0
    for n in nums:
        if n != min_:
            count += n - min_
    return count
