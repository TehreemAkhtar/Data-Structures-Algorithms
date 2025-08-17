# SOURCE: Leetcode
# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Solution: https://neetcode.io/solutions/longest-consecutive-sequence


# Sort solution

# Time Complexity (TC): O(n log n):
# Space Complexity (SC): O(n) or O(1): Depends on sorting algo
# Approach: sort the entire array and start the counting the sequence -> skip duplicates ->
# reset the count for new sequence
def longest_consecutive_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()

    curr_count = 0
    max_count = 0

    if len(nums) in {1, 0}:
        return len(nums)

    for i in range(len(nums) - 1):
        if nums[i + 1] == nums[i]:
            continue
        elif nums[i + 1] != nums[i] + 1:
            curr_count = 0
        else:
            curr_count += 1
        max_count = max(max_count, curr_count)

    return max_count + 1


# Hash set solution

# Time Complexity (TC): O(n): the entire sequence is traversed once across the whole algorithm, not once per element.
# Though the solution may look like quadratic due to the while loop inside the for loop, the while loop only gets
# executed at the start of a sequence when (n-1) is not found in the set. Worst case for a sorted array,
# the first pass will run the while loop (n-1) times, but all other run it will not get executed at all.
# so the while loop will only run a total of n times for the entire length of the solution.
# so the complexity is O(n+n) which is O(n)..

# Space Complexity (SC): O(n): We can avoid this by directly updating input array to a set
# Approach: Convert to set for faster lookups and avoid duplicates -> only start counting the sequence if
# no left neighbour is found -> iterate over the whole sequence until a new sequence is found ->
# update the streak for whatever the max streak is
def longest_consecutive_2(nums):
    """
    :type nums: List[int]¬
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
