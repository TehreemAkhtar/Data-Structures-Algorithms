# SOURCE: Leetcode
# https://leetcode.com/problems/product-of-array-except-self/description/
# Solution: https://neetcode.io/solutions/product-of-array-except-self

# Solution # 1
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
# Approach: calculate prefix + suffix sum -> then multiply those excluding current num

def product_except_self_1(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    prefix_sum = calculate_prefix_sum(nums)
    suffix_sum = calculate_suffix_sum(nums)

    for i in range(len(nums)):
        j, k = i - 1, i + 1
        if i == 0:
            res.append(suffix_sum[k])
        elif i == len(nums) - 1:
            res.append(prefix_sum[j])
        else:
            res.append(suffix_sum[k] * prefix_sum[j])
    return res


def calculate_prefix_sum(nums):
    res = []
    prod = 1
    for i, n in enumerate(nums):
        prod *= n
        res.append(prod)
    return res


def calculate_suffix_sum(nums):
    res = [1] * len(nums)
    prod = 1
    for i in range(len(nums) - 1, -1, -1):
        prod *= nums[i]
        res[i] = prod
    return res


# Solution # 2
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
# Approach: A more concise way with same approach #1
def product_except_self_2(nums):
    n = len(nums)
    res = [0] * n
    pref = [0] * n
    suff = [0] * n

    pref[0] = suff[n - 1] = 1
    for i in range(1, n):
        pref[i] = nums[i - 1] * pref[i - 1]
    for i in range(n - 2, -1, -1):
        suff[i] = nums[i + 1] * suff[i + 1]
    for i in range(n):
        res[i] = pref[i] * suff[i]
    return res


# Solution # 3
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n) for only the output array
# Approach: Use 1 output array to calculate prefix sum then multiply the postfix within the same and return

def product_except_self_3(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    res = [1] * n
    prefix = postfix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res
