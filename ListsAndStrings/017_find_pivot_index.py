# SOURCE: Leetcode
# https://leetcode.com/problems/find-pivot-index/
# Solution: https://www.youtube.com/watch?v=u89i60lYx8U (Neetcode)

# Solution # 1
def pivot_index_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    prefix_sum = []
    total_sum = 0
    for n in nums:
        total_sum += n
        prefix_sum.append(total_sum)

    for i in range(len(nums)):
        left_sum = prefix_sum[i - 1] if i > 0 else 0
        right_sum = total_sum - prefix_sum[i] if i != len(nums) - 1 else 0
        if left_sum == right_sum:
            return i
    return -1
