# SOURCE: Leetcode
# https://leetcode.com/problems/koko-eating-bananas/description/
# Solution: https://neetcode.io/solutions/koko-eating-bananas
import math

# Time Complexity (TC): O(log max(piles) * len(piles)): Binary Search is performed over the possible eating speeds [1, max(piles)].
# Space Complexity (SC): O(1): Only a few variables are used.

# Approach:
# - The possible eating speeds lie in the range [1, max(piles)].
# - Use Binary Search to find the minimum valid eating speed.
# - For each candidate speed k, compute the total hours needed to eat all piles.
# - If total_hours > h, the speed is too slow, so search the right half.
# - Otherwise, k is a valid speed. Record it and continue searching the left half
#   to see if an even smaller valid speed exists.
def min_eating_speed_1(piles, h):
    l = 1
    r = max(piles)
    min_k = float("inf")

    while l <= r:
        k = (l + r) // 2
        total_hours = 0
        for p in piles:
            total_hours += math.ceil(p / k)

        if total_hours > h:
            l = k + 1
        else:
            r = k - 1
            min_k = min(min_k, k)

    return min_k


# Since binary search guarantees that after the loop l points to the smallest valid eating speed,
# you don’t even need min_k
def min_eating_speed_optimised(piles, h):
    l = 1
    r = max(piles)

    while l <= r:
        k = (l + r) // 2
        total_hours = sum(math.ceil(p / k) for p in piles)
        if total_hours > h:
            l = k + 1
        else:
            r = k - 1

    return l