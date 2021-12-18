
# Space: O(n)
# Time: O(n)

class Solution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1: return 1 if matrix[0][0] == '1' else 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for y in range(m):
            for x in range(n):
                if y == 0 or x == 0:
                    dp[y][x] = int(matrix[y][x])
                elif matrix[y][x] == '1':
                    dp[y][x] = min(dp[y][x - 1], dp[y - 1][x - 1], dp[y - 1][x]) + int(matrix[y][x])
                res = max(res, dp[y][x])
        return res * res




