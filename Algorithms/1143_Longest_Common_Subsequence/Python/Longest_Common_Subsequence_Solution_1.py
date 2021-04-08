
# Space: O(m*n)
# Time: O(m*n)

# Explanation:
# 1. build a board with len(text1) width and len(text2) length to record longest common subsequence at given point.
# 2. run a nested loop for these two strings,

#    if text1[i] == text[j], we found a matched character from both strings, we want to know what is the longest common
#    subsequence WITHOUT this matched character(which is at board[i-1][j-1]), then plus 1.
#    (if text1[i] == text[j]: board[i][j] = board[i-1][j-1]+1)

#    if text1[i] != text[j], we do not have matched character at this point, we want to know what is the longest common
#    subsequence WITHOUT this unmatched character(either from text1 or text2), then put it at current place.
#    (if text1[i] != text[j]: board[i][j] = max(board[i-1][j], board[i][j+1])

# 3. the result(longest common subsequence) located in bottom right corner of the board.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row_length = len(text1)
        column_length = len(text2)

        if row_length == 0 or column_length == 0:  # handle edge cases
            return 0

        board = [[0 for _ in range(row_length + 1)] for _ in range(column_length + 1)]
        # "+1" will reduce the coding complexity, otherwise we need to handle border cases.

        temp_text1 = '*' + text1  # add "*" to match the width of the board
        temp_text2 = '*' + text2  # add "*" to match the length of the board

        for column in range(1, column_length + 1):
            for row in range(1, row_length + 1):
                if temp_text2[column] == temp_text1[row]:
                    board[column][row] = board[column - 1][row - 1] + 1
                else:
                    board[column][row] = max(board[column - 1][row], board[column][row - 1])

        return board[-1][-1]


