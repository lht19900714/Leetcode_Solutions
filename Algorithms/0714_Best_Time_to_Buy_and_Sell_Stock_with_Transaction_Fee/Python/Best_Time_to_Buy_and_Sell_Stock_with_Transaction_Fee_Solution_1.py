
# Space: O(1)
# Time: O(n)

class Solution:
    def maxProfit(self, prices, fee):
        length = len(prices)
        if length <= 1: return 0

        cash, profit = -prices[0], 0

        for i in range(1, length):
            profit = max(profit, profit + prices[i] - fee)
            cash = max(cash, profit - prices[i])

        return profit




