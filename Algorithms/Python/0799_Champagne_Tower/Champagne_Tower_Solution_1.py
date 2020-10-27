
# Space: O(n)
# Time: O(n)

class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        if poured == 0: return 0

        # max row is 100
        dp = [[0 for _ in range(100 + 1)] for _ in range(100 + 1)]
        dp[0][0] = poured

        for i in range(query_row + 1):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    dp[i + 1][j + 1] += (dp[i][j] - 1) / 2
                    dp[i + 1][j] += (dp[i][j] - 1) / 2
                    dp[i][j] = 1

        return dp[query_row][query_glass]





