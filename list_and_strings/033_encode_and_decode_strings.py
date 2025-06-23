# SOURCE: Lintcode
# https://www.lintcode.com/problem/659/description
# Solution: https://www.youtube.com/watch?v=B1k_sxOSgv8


# Solution # 1
# Approach: Encode each string with this format: len-of-each-string + '#' + <actual-string>
# Reason we're also using '#' as a delim:
# Encode:
# Time Complexity (TC): O(n.k^2): Due to creating a copy of new str in loop as str is immutable. Cost grows
# with number of strings (N), and quadratically with average string length (K)
# Space Complexity (SC): O(n.k): where n is the combined length of everything

def encode_1(strs):
    encoded_str = ''
    for s in strs:
        # len(s) = O(1) because python stores len internally in built-in string
        # str(len(s)) = O(L); L is length of string. A digit has log₁₀(N). Converting a str->int takes O(logN) time
        # + s = O(L) -> copying s of length L
        # encoded_str += takes O(N) where N is the combined length of everything
        # Python because strings are immutable — each += makes a new string copy!
        encoded_str += str(len(s)) + '#' + s
    return encoded_str


# TC: O(n.k); n = length of strs, k = length of each str
# SC:O(n.k)
def encode_optimised(strs):
    encoded_str = ''.join([str(len(s)) + '#' + s for s in strs])
    return encoded_str


# Decode:
# Time Complexity (TC): O(n) or O(n.k): where N = total encoded string length, same as original total length
# Space Complexity (SC): O(n) or O(n.k): where n is the combined length of everything
def decode(s: str):
    res = []
    i = 0
    while i < len(s):
        # s[i:] = O(M): creates a new substring
        # split('#') = O(M): scans until it finds the first #
        # In total, all the characters are touched once across all iterations because i gets everytime.
        # So the total cost of all s[i:].split() is O(total length) — linear.
        num = s[i:].split('#')[0]
        i += len(num) + 1
        # int(num) = O(log K), This parsing time is negligible compared to slicing the full word of length K.
        # So for big K, the slicing dominates.
        # So overall per word: O(K) for slicing, O(log K) for parsing.
        s_len = int(num)
        # Slicing a substring of length K → O(K)
        # Again: each character is sliced exactly once.
        # So total slicing is also O(total length).
        res.append(s[i:i + s_len])
        i += s_len
    return res


# Solution # 2
# Approach: encode each string’s length as a single character, instead of writing the length as digits plus #
# There’s no # or digits — just a special hidden character whose code is the length. If your strings can be huge
# (like 10,000 characters), this trick needs multiple bytes to store the length — so the simple version fails.
def encode_2(strs):
    res = []
    for s in strs:
        # [char] is the single character whose Unicode code equals the length.
        # With chr() you can only store lengths up to 255 for 1-byte characters (\xFF). For larger strings, you
        # must switch to multi-byte encoding or more complex tricks (like storing length in 2 chars).
        res.append(chr(len(s)) + s)
    return ''.join(res)


def decode_2(s: str):
    res = []
    i = 0
    while i < len(s):
        length = ord(s[i])  # read the first char, get its code point = length
        i += 1
        res.append(s[i:i + length])
        i += length
    return res


# Solution # 3
# Approach: Use a fixed-size binary representation of the length instead of a text number plus a separator.
def encode_3(strs):
    encoded = b''  # a bytes object
    for s in strs:
        length = len(s)
        # use 4 bytes for the length, big-endian
        # with 4 bytes, you can safely encode strings up to ~4 billion characters long.
        # That’s usually more than enough for any real-world text.
        #  big-endian: how bytes are ordered when storing a number -> store the most significant byte first:
        encoded += length.to_bytes(4, 'big')
        encoded += s.encode('utf-8')
    return encoded


# In network protocols and binary formats, big-endian is common because it’s more intuitive: higher-order bits come first.

def decode_3(data):
    res = []
    i = 0
    while i < len(data):
        # read 4 bytes → convert back to int
        length = int.from_bytes(data[i:i + 4], 'big')
        i += 4
        # read the next `length` bytes → decode back to str
        s = data[i:i + length].decode('utf-8')
        res.append(s)
        i += length
    return res

# byte-array method is safer, especially when you care about binary storage and large lengths.
# For robust binary encoding → raw bytes is cleaner and predictable.

# Unicode character
# Uses a single Unicode character with code point equal to the length
# Good for lengths 0–255 (if using chr(x) for x ≤ 255); works like “one-character prefix”.

# VS

# Raw bytes
# Uses 1, 2, 4 bytes to store the binary integer value
# More robust: works for large lengths, not restricted to Unicode code points.

# 📍 Key difference
# 	•	Using chr(length):
# 	•	Stores the length as a single Unicode code point.
# 	•	In UTF-8, this means that character might expand to multiple bytes!
# For example, chr(200) → 'È' → which in UTF-8 takes 2 bytes.
# So it’s conceptually one character in Python, but in binary it’s still variable bytes in UTF-8.
# This can be tricky.
# 	•	Using length.to_bytes(...):
# 	•	Stores the length as exactly N bytes in binary.
# 	•	No character encoding step — no ambiguity.
# 	•	Robust, used in real binary protocols.


# Example:
# In computer networking, when you send data over the internet (or any network), you
# usually wrap the actual data with extra information called headers.
#
# Why?
# Because the receiver needs to know:
# 	•	How big is this chunk of data?
# 	•	What type of data is it?
# 	•	Where does it belong in a bigger message?
#
# So, the header acts like a label or instruction sheet for the data.
#
# When you encode multiple strings into a single string or byte blob:
# 	•	You do something similar:
# 	•	For each piece of text: The length is like a header — so when decoding, you know:
# “I’ll read 4 bytes to get the length → then read exactly that many bytes for the text.”
#
# So, you’re doing the same idea on a small scale:
# Add a “header” to each piece of text so the decoder can read it back correctly.
