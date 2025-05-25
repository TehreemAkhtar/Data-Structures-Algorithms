# SOURCE: Leetcode
# https://leetcode.com/problems/valid-anagram/description/
# Solution: https://neetcode.io/solutions/valid-anagram

# What is Unicode?
# Unicode is a universal character set — it assigns a unique number (called a code point) to every character
# in every language (like English, Arabic, Chinese), including emojis and symbols.
# But computers store everything as bytes (0s and 1s) — so we need a way to encode those code points into bytes.
# That’s where UTF-8, UTF-16, etc. come in.
# | Encoding   | Meaning                  | Size per character         | Good For                          |
# | ---------- | ------------------------ | -------------------------- | --------------------------------- |
# | **UTF-8**  | Variable-length encoding | 1–4 bytes per character    | Text in English + mixed languages |
# | **UTF-16** | Variable-length encoding | 2 or 4 bytes per character | Asian languages, emoji-heavy text |
# | **UTF-32** | Fixed-length encoding    | 4 bytes per character      | Simplicity (but uses more memory) |

# ✅ Which One to Use?
# UTF-8 is the most common — used on the web, in Python, and in most modern systems.
# UTF-16 is used internally in some systems (like Windows, Java).
# UTF-32 is used less often due to high memory cost.

# 🎯 How to reason (not memorize):
# 🧠 Think of the number at the end as a clue:
#
# UTF-8 → “8-bit chunks” (1 byte chunks)
# UTF-16 → “16-bit chunks” (2 byte chunks)
# UTF-32 → “32-bit chunks” (4 byte chunks)


# Solution # 1
# Time Complexity (TC): O(n log n): Python uses Tim sort which takes n log n time
# Space Complexity (SC): O(n): Strings in Python are immutable. Therefore, when you sorted(s)
# Approach: Converts s into a list of characters -> Sorts that list -> Returns a new sorted list
# Even though it feels like you're not explicitly creating anything, under the hood,
# a copy of all elements is created. As a string can't be sorted in-place.
def is_anagram_1(s: str, t: str) -> bool:
    return False if len(s) != len(t) else sorted(s) == sorted(t)


import unicodedata


# To handle such multi-code-point graphemes properly: It's important to normalise strings for unicode chars
def is_anagram_1_unicode(s, t):
    # len check should be avoided because of multi-byte unicode chars e.g.
    # s = "á"   # 'a' + combining acute accent → U+0061 + U+0301: len=2
    # t = "á"  : len=1
    # NOTE: we can use only use this check once input is normalised
    s = unicodedata.normalize('NFC', s)
    t = unicodedata.normalize('NFC', t)
    # NFC: composes characters to a canonical form (e.g., 'a' + '´' becomes 'á')
    # NFD: decomposes them (e.g., 'á' becomes 'a' + '´')
    # Pick one form consistently for both strings.
    return sorted(s) == sorted(t)


# ✅ Rule of Thumb
# If you're comparing machine-level bytes or raw sequences: don't normalize.
# If you're comparing human-readable text or working with anagrams/words:
# normalize first so visually identical characters match.


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


def is_anagram4_unicode_safe(s, t: str) -> bool:
    s = unicodedata.normalize('NFC', s)
    t = unicodedata.normalize('NFC', t)

    if len(s) != len(t):
        return False

    count = {}

    for ch_s, ch_t in zip(s, t):
        count[ch_s] = count.get(ch_s, 0) + 1
        count[ch_t] = count.get(ch_t, 0) - 1

    return all(v == 0 for v in count.values())


# Solution # 5
# Optimisation of Sol #3- using a list instead of a dict
# Limitation: will break if input contains anything other than a-z letters i.e. not suitable for unicode chars
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


from collections import Counter


def is_anagram_6(s, t: str) -> bool:
    s = unicodedata.normalize('NFC', s)
    t = unicodedata.normalize('NFC', t)
    return Counter(s) == Counter(t)
