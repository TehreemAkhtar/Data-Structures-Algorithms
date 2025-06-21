# SOURCE: Leetcode
# https://leetcode.com/problems/group-anagrams/description/
# Solution: https://www.youtube.com/watch?v=vzdNOK2oB2E
from collections import defaultdict


# Time Complexity (TC): O(n klogk): k = length of string: n = length of list containing strings (mean n times)
# Space Complexity (SC): O(k.n):
# Approach: as sorted strings can be compared easily for anagrams so sort each string and store it as
# hashmap key and with each sorted string equal to key => store the original str reference as a value in list
def group_anagrams_1(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    res = defaultdict(list)
    for s in strs:
        # TC: for each string = O(k log k) => for n strings = O(n klogk)
        # SC: Keys: Up to N unique sorted strings ⇒ O(NK) total characters.
        # 	  Values: Lists whose total length is exactly N (one reference per input string) ⇒ negligible, just pointers.
        sorted_s = ''.join(sorted(s))
        res[sorted_s].append(s)
    return list(res.values())


# Time Complexity (TC): O(n k): k = length of string: n = length of list containing strings (mean n times)
# Space Complexity (SC): O(n): because
# Each key is a tuple of 26 integers, representing the letter counts for a word.
# 	•	E.g. 'abb' → (1, 2, 0, ..., 0)
# 	•	So each key uses 26 integers = O(1) (since alphabet size is constant).
# 	•	If all words are different anagram groups, you have N keys max.
# Keys = O(N)
# Values = O(N)
# Output = O(N)
# Total = O(N)
# This version does not store sorted copies of each string!
# Instead, it stores an O(1) tuple as key for each word.
# Therefore, no K factor from storing full strings as keys.

# Approach: As input only contains a-z chars so we have 26 chars in total. We can use frequency count method.
# Anagrams will have same frequency hence list -> tuple -> use as dict key and append strings with same frequency
# in hashmap
def group_anagrams_2(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        print(tuple(count))
        res[tuple(count)].append(s)
    print(res)
    return list(res.values())

# Some notes:
# Space Complexity:
# The algorithm will take more space on the solution of frequency map than the sorting solution if
# the strings do not have many characters.
# If your strings are short — say, < 26 letters — the tuple key uses more raw memory (28 bytes per int = 26 * 26 bytes)
# in Python than storing the sorted string.
#  If your strings are long — say, 1000 letters — then the sorted string key is much bigger than the
#  constant-size tuple.

# IMP => So, in other words, if you see that the string length is specified as having the possibility of being very
# large then the frequency map is the way to go, otherwise the sorting algorithm is the best solution.

# Time Complexity:
#  for tiny K, sorting can be a tiny bit faster in practice because the overhead for creating the tuple key
#  and hashing it can be more expensive than sorting just 1 or 2 letters
# Very small K (1–3): sorting is fine and simple
# Large K (long strings): frequency map is clearly better
