
# Space: O(n)
# Time: O(n)


class Solution:
    def winnerSquareGame(self, n):
        dp = [False] * n + 1

        for i in range(1, n + 1):
            for j in range(1, int(pow(i, 0.5)) + 1):
                if dp[i - j * j] is False:
                    dp[i] = True
                    break

        return dp[n]




