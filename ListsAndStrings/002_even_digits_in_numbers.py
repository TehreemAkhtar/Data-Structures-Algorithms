# SOURCE: Leetcode
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/editorial/?source=submission-ac
from typing import List


#  -- Assuming numbers are non-negative

# Solution # 1
# Approach: Extract digits of each num using repeated division -> check parity -> increment counter accordingly
def has_even_digits(num: int) -> bool:
    digit_count = 0
    while num:
        digit_count += 1
        num //= 10
    return not digit_count & 1


def count_even_numbers(nums: List[int]) -> int:
    return sum(1 for num in nums if has_even_digits(num))
