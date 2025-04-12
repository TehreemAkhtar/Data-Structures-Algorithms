# SOURCE: Leetcode
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Solution: https://www.youtube.com/watch?v=XEmy13g1Qxc (Neetcode)
import heapq


# Solution # 1
# Time Complexity (TC): Avg case: O(n), Worst case: O(n2): uses quick select
# Space Complexity (SC): Avg case: O(log n), Worst case: O(n): Depends on depth of recursion stack ->
# which depends on the quality of pivot selection
# Approach: Uses QuickSelect - which is a slight modification of quick sort.
# The only difference is that in quick select, the quick sort algorithm is run on 1 part only
# depending on k.
class Solution(object):
    def find_kth_largest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quick_select(nums, 0, len(nums) - 1, k)

    def quick_select(self, nums, start, end, k):
        if start <= end:
            p_index = self.partition(nums, start, end)
            if len(nums) - k == p_index:
                return nums[p_index]
            if len(nums) - k > p_index:
                return self.quick_select(nums, p_index + 1, end, k)
            else:
                return self.quick_select(nums, start, p_index - 1, k)

    def partition(self, nums, start, end):
        pivot = nums[end]
        p_index = start
        for i in range(start, end):
            if nums[i] <= pivot:
                nums[i], nums[p_index] = nums[p_index], nums[i]
                p_index += 1
        nums[p_index], nums[end] = nums[end], nums[p_index]
        return p_index


# Solution # 2
# Time Complexity (TC): Avg case: O(n), Worst case: O(n2): uses quick select with optimisation
# Space Complexity (SC): Avg case: O(log n), Worst case: O(n): Depends on depth of recursion stack ->
# which depends on the quality of pivot selection
# Approach: Uses 3-way partitioning logic and skips duplicate elements.
class Solution2(object):
    def find_kth_largest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quick_select(nums, 0, len(nums) - 1, k)

    def quick_select(self, nums, start, end, k):
        if start <= end:
            lt, gt = self.partition(nums, start, end)
            if lt <= len(nums) - k <= gt:
                return nums[lt]
            if len(nums) - k > gt:
                return self.quick_select(nums, gt + 1, end, k)
            else:
                return self.quick_select(nums, start, lt - 1, k)

    def partition(self, array, start, end):
        pivot = array[end]
        i = lt = start
        gt = end

        while i <= gt:
            if array[i] < pivot:
                array[i], array[lt] = array[lt], array[i]
                lt += 1
                i += 1
            elif array[i] > pivot:
                array[i], array[gt] = array[gt], array[i]
                gt -= 1
            else:
                i += 1
        return lt, gt


# Solution # 3
# Time Complexity (TC): O(n logk): Traversing the array of size n.
# Each heappush() or heappop() on a heap of size k takes O(log k) time.
# Space Complexity (SC): O(k): Heap stores k elements only
# Approach: Uses a min heap to store k largest elements. Traverse the array and
# keep pushing elements until the heap reaches k+1 size. Once it reaches k+1, remove the root node,
# which will always be the smallest of all and our heap will contain k largest elements.
def find_kth_largest_3(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]


# Optimisation: Instead of always popping elements from the heap, we'll only pop/push when required
def find_kth_largest_3_optimised(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if min_heap[0] < num:
            heapq.heappushpop(min_heap, num)
    return min_heap[0]


# Solution # 4
# Time Complexity (TC): O(n + k log n)
# Space Complexity (SC): O(n): max heap size
# Approach: Negate the values to use Python’s heapq which is a min-heap by default ->
# Extract elements until you reach the kth element -> Negate the number again while returning it.
def find_kth_largest_4(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)   #O(n) - building the heap

    for _ in range(k - 1):
        heapq.heappop(max_heap)  #klogn - extracting the k largest elements.
    return -max_heap[0]
