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
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
    return list(res.values())
