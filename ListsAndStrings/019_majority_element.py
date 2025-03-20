# SOURCE: Leetcode
# https://leetcode.com/problems/majority-element
# Solution: https://www.youtube.com/watch?v=7pnhv842keE (Neetcode)


# Solution # 1
# Time Complexity (TC): O(n): Traverses the list in linear time and count frequency
# Space Complexity (SC): O(n): uses a hashmap to count frequency of each element
# Approach: In each iteration, update frequency in a hashmap and return as soon as the majority element is found
def majority_element_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maj_element = len(nums) // 2
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
        if count[n] > maj_element:
            return n


# Solution # 2
# Time Complexity (TC): O(n): calculates majority element in one pass
# Space Complexity (SC): O(1): Uses a single variable
# Approach: Uses Boyer Moore Majority Vote algorithm
# Link: https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/
# Picks first element as a candidate. If the next element is equal to the candidate, we increment the counter.
# If not, its decremented. Once the counter reaches 0, we update candidate i.e. the element with the curr element.
# The only condition for this to work in one pass is: There should always exist a majority element.
# Otherwise, traverse the array one more time to make sure if selected candidate is the majority element.
def majority_element_2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 1
    res = nums[0]

    for i in range(1, len(nums)):
        if count == 0:
            res = nums[i]
        if res == nums[i]:
            count += 1
        else:
            count -= 1

    return res


# This is the second pass to confirm the majority element. In either case, the algorithm takes linear time
def second_pass_to_confirm_majority_element(nums, candidate):
    count = sum(nums[i] == candidate for i in range(len(nums)))
    return candidate if (count > len(nums) // 2) else -1
