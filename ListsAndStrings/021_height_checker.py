# SOURCE: Leetcode
# https://leetcode.com/problems/height-checker/


# Solution # 1
# Time Complexity (TC): O(nlogn): Python sort function uses Tim sort - nlogn
# Space Complexity (SC): O(n): uses an extra array to keep the sorted list
# Approach: create a sorted version of input and then start comparing elements in each iteration
def height_checker_1(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    expected = sorted(heights)
    return sum(1 for i in range(len(heights)) if heights[i] != expected[i])


# Solution # 2
# Time Complexity (TC): O(n+k): uses count sort as the array elements are restricted to 100 (represented as k)
# Space Complexity (SC): O(n): uses an extra array to keep the frequency count
# Approach: create an array of size equal to the max number in constraint and count frequency of each number.
# Iterate the heights array and start with number 1 (smallest element that can occur in array), compare with
# height and update mismatch. Also update the frequency of the numbers that have been checked, so we can update
# the current_element.
def height_checker_2(heights):
    frequency = [0] * 101
    for h in heights:
        frequency[h] += 1

    current_expected = 1
    mismatch = 0

    for h in heights:
        while current_expected <= 100 and frequency[current_expected] == 0:
            current_expected += 1

        if h != current_expected:
            mismatch += 1

        frequency[current_expected] -= 1
    return mismatch
