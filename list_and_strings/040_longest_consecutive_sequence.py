# SOURCE: Leetcode
# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Solution: https://neetcode.io/solutions/longest-consecutive-sequence



# Sort solution
# Time Complexity (TC): O(n): the entire sequence is traversed once across the whole algorithm, not once per element.
# Space Complexity (SC): O(n): We can avoid this by directly updating input array to a set
# Approach:
def longest_consecutive_2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_set = set(nums)
    streak = 0

    for n in num_set:
        # This ensures that we only start the while loop at the beginning of a sequence.
        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            # Inner while loop total across all iterations: also O(n) because every number is visited at
            # most once in a consecutive walk and skipped for the numbers which don't start a sequence
            streak = max(streak, length)
    return streak


# Hash set solution
# Time Complexity (TC): O(n): the entire sequence is traversed once across the whole algorithm, not once per element.
# Space Complexity (SC): O(n): We can avoid this by directly updating input array to a set
# Approach:
def longest_consecutive_2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_set = set(nums)
    streak = 0

    for n in num_set:
        # This ensures that we only start the while loop at the beginning of a sequence.
        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            # Inner while loop total across all iterations: also O(n) because every number is visited at
            # most once in a consecutive walk and skipped for the numbers which don't start a sequence
            streak = max(streak, length)
    return streak
