
# Space: O(n)
# Time: O(n)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1: return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        temp_board = [[0 for _ in range(n)] for _ in range(m)]
        temp_board[0][0] = 1

        for y in range(m):
            for x in range(n):
                if obstacleGrid[y][x] != 1:
                    temp_board[y][x] += temp_board[y - 1][x] if y - 1 >= 0 else 0
                    temp_board[y][x] += temp_board[y][x - 1] if x - 1 >= 0 else 0

        return temp_board[m - 1][n - 1]




