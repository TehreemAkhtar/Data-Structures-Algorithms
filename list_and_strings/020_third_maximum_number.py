# SOURCE: Leetcode
# https://leetcode.com/problems/third-maximum-number
# Solution: https://leetcode.com/problems/third-maximum-number/editorial/

# Solution # 1
# Time Complexity (TC): O(n): Traverses the list in linear time and count frequency
# Space Complexity (SC): O(1): uses a hashmap to count frequency of each element
# Approach: In each iteration, update frequency in a hashmap and return as soon as the majority element is found
def third_max_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = list(set(nums))

    first_max = max(nums)
    nums.remove(first_max)
    try:
        second_max = max(nums)
        nums.remove(second_max)

        third_max = max(nums)
        nums.remove(third_max)
    except ValueError:
        return first_max
    return third_max

# Rest of the solutions can be read from LC editorial
