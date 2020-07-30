
# Space: O(n)
# Time: O(n)


class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        if length <= 1: return 0

        # initial three array to record best profit for three different transactions.
        cooldown = [0] * (length + 1)
        sell = [0] * (length + 1)
        hold = [0] * (length + 1)

        hold[0] = -float('inf')

        # align prices array to the other array for better understanding.
        prices = [None] + prices

        for i in range(1, length + 1):
            # HOLD transaction: the best profit on day i is from either previous hold day or previous cooldown day with purchase on day i
            hold[i] = max(hold[i - 1], cooldown[i - 1] - prices[i])

            # SELL transaction: the best profit on day i is from previous hold day will sell on day i
            sell[i] = hold[i - 1] + prices[i]

            # COOLDOWN transaction: the beast profit on day i is from previous cooldown day or previous sell day
            cooldown[i] = max(cooldown[i - 1], sell[i - 1])

        # the final solution will from either sell or cooldown transaction
        return max(sell[-1], cooldown[-1])



