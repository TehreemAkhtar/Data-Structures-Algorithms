# SOURCE: Leetcode
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/editorial/?source=submission-ac
from typing import List


# Solution#1
def hasEvenDigits(num: int) -> bool:
    digit_count = 0
    while num:
        digit_count += 1
        num //= 10
    return digit_count & 1 == 0


def findNumbers(nums: List[int]) -> int:
    # Counter to count the number of even digit integers
    even_digit_count = 0

    for num in nums:
        if hasEvenDigits(num):
            even_digit_count += 1

    return even_digit_count
