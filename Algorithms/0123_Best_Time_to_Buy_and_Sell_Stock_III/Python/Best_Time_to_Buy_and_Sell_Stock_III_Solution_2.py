
# Space: O(n)
# Time: O(n)


class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        if length <= 1:
            return 0

        # initial status array
        # hold_1: result on each day when we decided to buy/hold first stock
        # sold_1: result on each day when we decided to sell first stock
        # hold_2: result on each day when we decided to buy/hold second stock
        # sold_2: result on each day when we decided to sell second stock

        hold_1, sold_1, hold_2, sold_2 = [-float('inf')]*length, [0]*length, [-float('inf')]*length, [0]*length

        for i in range(length):
            if i == 0:  # handle day 1 manually
                hold_1[i], sold_1[i], hold_2[i], sold_2[i] = -prices[i], 0, hold_2[i], 0
            else:
                hold_1[i] = max(hold_1[i - 1], -prices[i])
                sold_1[i] = max(sold_1[i - 1], hold_1[i - 1] + prices[i])
                hold_2[i] = max(hold_2[i - 1], sold_1[i - 1] - prices[i])
                sold_2[i] = max(sold_2[i - 1], hold_2[i - 1] + prices[i])

        return max(sold_1[-1], sold_2[-1])




