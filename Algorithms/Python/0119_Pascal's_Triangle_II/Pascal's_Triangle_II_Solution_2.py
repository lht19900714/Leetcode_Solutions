
# Space: O(n^2)
# Time: O(n^2)


class Solution:
    def getRow(self, rowIndex):
        board = [[1 for _ in range(rowIndex + 1)] for _ in range(rowIndex + 1)]

        for i in range(rowIndex + 1):
            for j in range(i):
                if j == 0:
                    continue
                else:
                    board[i][j] = board[i - 1][j] + board[i - 1][j - 1]

        return board[rowIndex]






