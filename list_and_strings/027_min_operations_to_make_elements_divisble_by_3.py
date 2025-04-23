# SOURCE: Leetcode
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three


# Solution # 1
# Time Complexity (TC): O(n):
# Space Complexity (SC): O(1): No extra memory
# Approach: Always gives you the minimum number of +1 or -1 operations to make x divisible by 3.
# Any number x can have a remainder of either 0, 1, or 2 when divided by 3:
# If x % 3 == 0, it’s already divisible by 3 → needs 0 operations ✅
# If x % 3 == 1, you can either:
# Subtract 1 → x - 1 is divisible by 3 → 1 operation
# Add 2 → x + 2 is divisible by 3 → 2 operations
# So: min(1, 3 - 1) = min(1, 2) = 1
def minimum_operations_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    return sum((min(n % 3, 3 - (n % 3))) for n in nums)


# Simple version of 1
def minimum_operations_2(nums):
    count = 0
    for n in nums:
        if n % 3 != 0:
            if (n + 1) % 3 == 0:
                count += 1
            elif (n - 1) % 3 == 0:
                count += 1
    return count

# TIP: Just count 1 every time if not divisible by 3.
