# SOURCE: Leetcode
# https://leetcode.com/problems/valid-anagram/description/
# Solution: https://neetcode.io/solutions/valid-anagram


# Solution # 1
# Time Complexity (TC): O(n log n): Python uses Tim sort which takes n log n time
# Space Complexity (SC): O(n): Strings in Python are immutable. Therefore, when you sorted(s)
# Approach: Converts s into a list of characters -> Sorts that list -> Returns a new sorted list
# Even though it feels like you're not explicitly creating anything, under the hood,
# a copy of all elements is created. As a string can't be sorted in-place.
def is_anagram_1(s: str, t: str) -> bool:
    return False if len(s) != len(t) else sorted(s) == sorted(t)


# Solution # 2
# Time Complexity (TC): O(n): sort + traversing the array
# Space Complexity (SC): Assuming only alphabets are considered = O(1): since we have at most 26 different characters.
# BUT if unicode chars are included; which are 150k+ then SC will be O(n)
# Approach: Count frequency of each char in two dicts and compare them
def is_anagram_2(s, t: str) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    return count_s == count_t


# Solution # 3
# Optimisation - using only 1 hashmap
# Time Complexity (TC): O(n): sort + traversing the array
# Space Complexity (SC): O(1) or O(n) depending on input
# Approach: use a single dict count to increment for s[i] and decrement for t[i]. So by the end of the loop:
# If s and t are true anagrams, every character’s count will be 0.
def is_anagram_3(s, t: str) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    count = {}

    for i in range(len(s)):
        count[s[i]] = 1 + count.get(s[i], 0)
        count[t[i]] = 1 - count.get(t[i], 0)
    return all(v == 0 for v in count.values())


# Solution # 4
# Optimisation of Sol #3- using zip avoids unnecessary indexing
def is_anagram_4(s, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    for ch_s, ch_t in zip(s, t):
        count[ch_s] = count.get(ch_s, 0) + 1
        count[ch_t] = count.get(ch_t, 0) - 1

    return all(v == 0 for v in count.values())


# Solution # 5
# Optimisation of Sol #3- using a list instead of a dict
# Limitation: will break if input contains anything other than a-z letters.
# SC: O(1), TC: O(n)
def is_anagram_5(s, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26

    for ch_s, ch_t in zip(s, t):
        # We subtract 'a' to normalize the alphabet. We use this to map letters to indices from 0 to 25
        # e.g. ord('c') - ord('a') = 99 - 97 = 2
        count[ord(ch_s) - ord('a')] += 1
        count[ord(ch_t) - ord('a')] -= 1

    return all(v == 0 for v in count)
