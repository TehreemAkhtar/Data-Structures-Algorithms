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