
# Space: O(n)
# Time: O(n)

class Solution:
    def maxAreaOfIsland(self, grid):
        self.res = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(board, y, x, m, n):
            if not (0 <= y < m and 0 <= x < n): return 0
            if board[y][x] == 0: return 0
            res = 0
            if board[y][x] == 1:
                board[y][x] = 0
                res += 1
            res += dfs(board, y, x - 1, m, n)
            res += dfs(board, y, x + 1, m, n)
            res += dfs(board, y - 1, x, m, n)
            res += dfs(board, y + 1, x, m, n)

            return res

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    self.res = max(self.res, dfs(grid, y, x, m, n))
        return self.res





