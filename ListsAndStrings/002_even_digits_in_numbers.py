# SOURCE: Leetcode
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/editorial/?source=submission-ac
from typing import List


#  -- Assuming numbers are non-negative

# Solution # 1

# Time Complexity (TC): O(n log m)
# Space Complexity (SC): O(1)
# Approach: Extract digits of each num using repeated division -> check parity -> increment counter accordingly
def has_even_digits(num: int) -> bool:
    digit_count = 0
    while num:
        digit_count += 1
        num //= 10
    return not digit_count & 1


def count_even_numbers(nums: List[int]) -> int:
    return sum(1 for num in nums if has_even_digits(num))


# Time Complexity Explanation (Reference: ChatGPT)

# How Do We Know the Number of Digits in a Number?
# A number has d digits if it falls within a certain range of values:
# If a number has 1 digit, it’s between 1 and 9 (or 10⁰ to 10¹ - 1).
# If a number has 2 digits, it’s between 10 and 99 (or 10¹ to 10² - 1).
# If a number has 3 digits, it’s between 100 and 999 (or 10² to 10³ - 1).
# This pattern tells us: A number with d digits lies in the range: 10^(d-1) <= num < 10^d


# What Happens When We Take Log10?
# The logarithm base 10 (log10) tells us the power of 10 needed to reach a number. For example:
# log10(100) = 2 because 100 = 10²
# log10(500) ≈ 2.7 because 500 is between 10² and 10³

# Why Does This Work?
# The logarithm essentially "measures" how many times we can divide the number by 10 before it gets smaller than 1.
# That’s exactly what counting digits does: it tells us how "big" a number is in base-10.

# How Long Does It Take to Count Digits of One Number?
# When you divide a number num by 10 repeatedly, the number of divisions required is proportional to the number of digits in num.
# Mathematically, the number of digits in a number is log10(num).
# Why? Because:
#
# In base-10, if a number has d digits, then it lies in the range 10^(d-1) to 10^d - 1.
# Taking the logarithm, the number of digits is roughly log10(num).

# Why Isn’t It O(N²)?
# O(N²) happens when you have nested loops where each loop runs in O(N). But here:
# The outer loop runs N times (one for each number).
# The inner operation (digit counting) runs O(logM) for each number.
# These two do not multiply to give N² because the inner loop isn't based on N, it's based on M.


# Solution # 2

# Time Complexity (TC): O(n log m)
# Space Complexity (SC): O(log m)
# Approach: Extract digits of each num using repeated division -> check parity -> increment counter accordingly

def count_even_numbers(nums: List[int]) -> int:
    count = 0
    for num in nums:
        length = len(str(num))
        if length & 1 == 0:
            count += 1
    return count


# Time Complexity Explanation
# We’ll analyze the time complexity step by step:
#
# 1. Outer for loop
#
# The for loop iterates over all the numbers in the list nums.
# If nums contains N numbers, the loop runs N times.

# 2. Converting num to a string (str(num))
#
# For each number, str(num) converts the integer into a string.
# The time complexity for converting a number to a string is proportional to the number of digits in the number.
# If the number has D digits, the time complexity of str(num) is O(D).
# The largest number in the list has at most log10(M) digits, where M is the largest number in the list.

# 3. Calculating len(str(num))
#
# After converting the number to a string, len() finds the length of the string.
# This operation takes O(1) time because the length is stored as a property of the string.

# 4. Overall time complexity for each number
#
# The dominant operation here is str(num), which takes O(log10(M)) time.
# For N numbers, the total time complexity is: O(N⋅logM)

# Space Complexity Explanation
# We’ll now analyze how much extra memory this solution uses:
#
# 1. String conversion (str(num))
#
# When you call str(num), Python creates a string representation of the number.
# The string requires memory proportional to the number of digits in the number. Although this is not
# explicitly stored in a var but this doesn't mean it doesn't consume memory. Python temporarily stores it
# memory for the len() func to compute its length. Once len() finishes its work,
# python garbage collector frees up the memory.
# For a number with D digits, the string will take O(D) space.
# Since the largest number has at most log10(M) digits, the space used for one string is O(log M).

# 2. Count variable
#
# The count variable is just an integer that gets incremented, so it takes O(1) space.
# 3. Total space complexity
#
# At any given time, only one string (from str(num)) exists in memory.
# Therefore, the total space complexity is: O(logM)

