
# Space: O(n)
# Time: O(n)

class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in coins:
            for j in range(len(dp)):
                if j - i >= 0:
                    dp[j] = min(dp[j], dp[j - i] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1





