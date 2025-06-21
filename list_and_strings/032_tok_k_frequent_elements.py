# SOURCE: Leetcode
# https://leetcode.com/problems/top-k-frequent-elements/description/
# Solution: https://www.youtube.com/watch?v=YPTqKIgVk-k


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
