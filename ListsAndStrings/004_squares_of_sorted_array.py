# SOURCE: Leetcode
# https://leetcode.com/problems/squares-of-a-sorted-array


# Solution # 1

# Time Complexity (TC): O(n log n)
# Space Complexity (SC): O(n) because of sorting algo: Tim Sort
# Approach: Traverse the entire array -> calculate square -> sort using python built-in function
def squares_of_sorted_array_1(nums):
    length = len(nums)
    for i in range(length):
        nums[i] = nums[i] * nums[i]
    # TC of python built-in func is O(N log N)
    # Uses Timsort, a hybrid sorting algorithm derived from merge sort and insertion sort.
    nums.sort()
    return nums


# Solution # 2

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1) because of sorting algo: Tim Sort
# Approach: Use two pointer technique
def squares_of_sorted_array_2(nums):
    pass
