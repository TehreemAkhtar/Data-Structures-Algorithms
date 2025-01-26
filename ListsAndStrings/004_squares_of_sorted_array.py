# SOURCE: Leetcode
# https://leetcode.com/problems/squares-of-a-sorted-array
# Solution: https://www.youtube.com/watch?v=FPCZsG_AkUg (Neetcode)


# Solution # 1

# Time Complexity (TC): O(n log n) because of Tim sort
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

# Time Complexity (TC): O(n log n) because of Tim sort
# Space Complexity (SC): O(n) because of sorting algo: Tim Sort
# Approach: Traverse the entire array -> calculate square -> sort using python built-in function
def squares_of_sorted_array_2(nums):
    return sorted(x * x for x in nums)


# Solution # 3

# Time Complexity (TC): O(n) because of Two Pointers Solution
# Space Complexity (SC): O(n) because of resultant arr
# Approach: Use two pointer technique because array is already sorted in non-decreasing order
# -> initialise one left and right most ptr -> compare both square val -> put the max one in resultant arr
# keep incrementing/decrementing ptrs -> keep appending left to the arr i.e. append in the start
def squares_of_sorted_array_3(nums):
    res = []
    l, r = 0, len(nums) - 1
    while l <= r:
        sq_l = nums[l] * nums[l]
        sq_r = nums[r] * nums[r]
        if sq_l > sq_r:
            res.append(nums[l])
            l += 1
        else:
            res.append(nums[r])
            r -= 1
    return res[::-1]
