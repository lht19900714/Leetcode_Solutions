
# Space: O(n)
# Time: O(n)

class Solution:
    def uniquePaths(self, m, n):
        board = [[0 for _ in range(n)] for _ in range(m)]
        for y in range(m):
            for x in range(n):
                if x == 0 or y == 0:
                    board[y][x] = 1
                else:
                    board[y][x] = board[y][x - 1] + board[y - 1][x]
        return board[-1][-1]




