
# Space: O(n)
# Time: O(n)


class Solution:

    def findPaths(self, m, n, maxMove, startRow, startColumn):
        self.mod = 1000000007
        self.board = [[[-1 for _ in range(n)] for _ in range(m)] for _ in range(maxMove + 1)]

        return self.dfs(m, n, startRow, startColumn, maxMove) % self.mod

    def dfs(self, row, column, y, x, n):
        if (not 0 <= y < row) or (not 0 <= x < column): return 1
        if (n == 0): return 0
        if self.board[n][y][x] > -1: return self.board[n][y][x]

        self.board[n][y][x] = (self.dfs(row, column, y - 1, x, n - 1)
                               + self.dfs(row, column, y, x - 1, n - 1)
                               + self.dfs(row, column, y + 1, x, n - 1)
                               + self.dfs(row, column, y, x + 1, n - 1))

        return self.board[n][y][x]




