# SOURCE: Leetcode
# https://leetcode.com/problems/k-items-with-the-maximum-sum/


# Time Complexity (TC): O(1): simple math operations
# Space Complexity (SC): O(1): no extra memory used
def k_items_with_maximum_sum(numOnes, numZeros, numNegOnes, k):
    """
    :type numOnes: int
    :type numZeros: int
    :type numNegOnes: int
    :type k: int
    :rtype: int
    """
    if k <= numOnes:
        return k
    if k <= (numOnes + numZeros):
        return numOnes
    else:
        return numOnes + ((k - (numOnes + numZeros)) * -1)