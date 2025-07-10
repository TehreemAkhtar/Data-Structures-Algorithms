# SOURCE: Leetcode
# https://leetcode.com/problems/valid-sudoku/
# Solution: https://neetcode.io/solutions/valid-sudoku
from collections import defaultdict


# Solution # 1
# Time Complexity (TC): O(n2): Iterate through every element in matrix
# Space Complexity (SC): O(n2): In worst case, a set can store every element i.e. n x n
# Approach: In a single nested loop: check every row, col and 3x3 box.
# To get a unique box: box_row // 3, box_col // 3
def is_valid_sudoku_1(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    grid_unique = {}
    for i in range(9):
        row_set = set()
        col_set = set()

        for j in range(9):
            if board[i][j].isdigit() and board[i][j] in row_set:
                return False
            if board[j][i].isdigit() and board[j][i] in col_set:
                return False

            row_set.add(board[i][j]) if board[i][j].isdigit() else None
            col_set.add(board[j][i]) if board[j][i].isdigit() else None

            if board[i][j].isdigit():
                box_row = i // 3
                box_col = j // 3

                box_indexes = [["b1", "b2", "b3"], ["b4", "b5", "b6"], ["b7", "b8", "b9"]]
                box_idx = box_indexes[box_row][box_col]
                if box_idx not in grid_unique:
                    grid_unique[box_idx] = []
                if board[i][j] in grid_unique.get(box_idx, []):
                    return False
                grid_unique[box_idx].append(board[i][j])
    return True


# Solution # 2
# Time Complexity (TC): O(n2): Iterate through every element in matrix
# Space Complexity (SC): O(n2): In worst case, a set can store every element i.e. n x n
# Approach: In a single nested loop: check every row, col and 3x3 box.
# To get a unique box: tuple (box_row // 3, box_col // 3)
def is_valid_sudoku_2(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    row = defaultdict(set)
    col = defaultdict(set)
    square = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in row[r]
                    or board[r][c] in col[c]
                    or board[r][c] in square[(r // 3, c // 3)]):
                return False

            row[r].append(board[r][c])
            col[c].append(board[r][c])
            square[(r // 3, c // 3)].append(board[r][c])
    return True


# Solution # 3
# Time Complexity (TC): O(n2): Iterate through every element in matrix
# Space Complexity (SC): O(n)
# Approach:
#   1.	For each cell:
# 	•	If it’s ".", skip
# 	•	Convert digit d to val = int(d) - 1
# 	2.	Check: Has 1 << val already been “seen” in row/col/box? using (1 << val) & cols[c] -> if already seen,
# 	the result will be non-zero else zero
# 	3.	If yes → Invalid board → return False
# 	4.	If no → mark it as seen by turning ON the bit
def is_valid_sudoku_3(board):
    rows = [0] * 9
    cols = [0] * 9
    squares = [0] * 9

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue

            val = int(board[r][c]) - 1
            if (1 << val) & rows[r]:
                return False
            if (1 << val) & cols[c]:
                return False
            if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                return False

            rows[r] |= (1 << val)
            cols[c] |= (1 << val)
            squares[(r // 3) * 3 + (c // 3)] |= (1 << val)

    return True
