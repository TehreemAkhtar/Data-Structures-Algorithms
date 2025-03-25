# SOURCE: Leetcode
# https://leetcode.com/problems/binary-search/
# Solution: https://www.youtube.com/watch?v=s4DPM8ct1pI (Neetcode)


# Solution # 1

# Time Complexity (TC): O(log n): binary search
# Space Complexity (SC): O(1)
# Approach: Use Binary Search
def search_1(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


# Solution # 2: Optimised version

# Time Complexity (TC): O(log n): binary search
# Space Complexity (SC): O(1)
# Approach: Use Binary Search
def search_2(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        # This problem won't occur in python because ints in python are unbounded can be infinitely large
        # but in cpp/java this can occur if an array is large enough such that our r and l can be equal to
        # a 32 bit int and adding them can cause overflow -> causing incorrect value in m
        mid = l + (r - l) // 2
        # This solution first gets the dist b/w l <-> r (r-l) -> (r - l)/2 will give half the distance
        # and adding it to l will give us the exact middle index
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

# TC Explanation: log(n) tell us how many times we have to divide a num by 2 for it to reach 1
