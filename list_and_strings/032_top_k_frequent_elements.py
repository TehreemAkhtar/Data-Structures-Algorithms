# SOURCE: Leetcode
# https://leetcode.com/problems/top-k-frequent-elements/description/
# Solution: https://www.youtube.com/watch?v=YPTqKIgVk-k
import heapq


# Time Complexity (TC): O(n + m.log.m) = O(nlgn) if there are n unique elements i.e. m = n
# Space Complexity (SC): O(m) or O(n) if m = n
# Approach: Use hashmap to count frequencies -> sort the hashmap based on values (frequencies) ->
# return the top k keys (indexes)
def top_k_frequent_1(nums, k):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_count[:k]]


# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
# Approach: Bucket sort -> items in buckets indexed by frequency → scan buckets in reverse → pick top K.
# Each index in freq represents the frequency and each element at freq[i] contains a bucket of numbers
# having that frequency.
def top_k_frequent_2(nums, k):
    count = {}
    # creating a list of buckets:
    freq = [[] for _ in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res


# Optimisation: Can keep track of max while creating count -> then use it to specify size of
# freq instead of using len(nums)


# Time Complexity (TC): O(nlogk) where k is the size of heap
# Space Complexity (SC): O(n + k) where k is the size of frequent elements
# Approach: Bucket sort -> items in buckets indexed by frequency → scan buckets in reverse → pick top K.
# Each index in freq represents the frequency and each element at freq[i] contains a bucket of numbers
# having that frequency.
def top_k_frequent_3(nums, k):
    count_dict = {}

    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1

    heap = []
    for key, value in count_dict.items():
        heapq.heappush(heap, (value, key))
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    for i in range(k):
        res.append(heapq.heappop(heap)[1])

    return res
# Time complexity breakdown:
# Min Heap idea
# 	•	Keep a Min Heap that never grows bigger than K:
# 	•	For each unique number: Push it in heap -> If heap size exceeds K, pop the smallest immediately.
# 	•	So at all times, heap size is at most K.
# 	After seeing all elements: (while creating res list)
# 	•	You pop K times → each pop is log K.
# 	For each of the N numbers:
# 	•	Push = log K (because heap is k)
# 	•	Possibly pop = log K
# 	•	So visiting all N = O(N log K)
# 	•   Final pops = O(K log K) but K is small
# 👉 So Total: O(N log K)

# Why we didn't use max-heap?
# Max Heap always works with the big heap (size N).
# Max Heap pops cost log(N) each
# And N is usually way bigger than K, so Min Heap is faster.
