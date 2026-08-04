# SOURCE: Leetcode
# https://leetcode.com/problems/search-a-2d-matrix/description/
# Solution: https://neetcode.io/solutions/search-a-2d-matrix



# Time Complexity (TC): O(log m.n): Treat the matrix as a sorted 1D array and perform Binary Search by
# mapping each 1D index back to its corresponding 2D row and column.
# Space Complexity (SC): O(1): Only a few variables are used.

# Approach:
# - Treat the matrix as a sorted 1D array of size rows * cols.
# - Initialize low = 0 and high = rows * cols - 1.
# - Compute the middle index and map it to 2D coordinates:
#       row = mid // cols
#       col = mid % cols
# - Compare the target with matrix[row][col] and narrow the search space
#   until the target is found or the search space is exhausted.
def search_matrix_1(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    low = 0
    high = (rows * cols) - 1

    while low <= high:
        mid = (low + high) // 2

        mid_r = mid // cols
        mid_c = mid % cols

        if target == matrix[mid_r][mid_c]:
            return True
        elif target > matrix[mid_r][mid_c]:
            low = mid + 1
        else:
            high = mid - 1

    return False

