
# Space: O(1)
# Time: O(n)

# same approach as solution 2, compress space complexity from n to 1.

class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        if length <= 1:
            return 0

        # initial status variable
        # hold_1: result on each day when we decided to buy/hold first stock
        # sold_1: result on each day when we decided to sell first stock
        # hold_2: result on each day when we decided to buy/hold second stock
        # sold_2: result on each day when we decided to sell second stock

        hold_1, sold_1, hold_2, sold_2 = -float('inf'), 0, -float('inf'), 0

        for i in range(length):
            temp_hold_1 = hold_1
            temp_sold_1 = sold_1
            temp_hold_2 = hold_2
            temp_sold_2 = sold_2

            hold_1 = max(temp_hold_1, -prices[i])
            sold_1 = max(temp_sold_1, temp_hold_1 + prices[i])
            hold_2 = max(temp_hold_2, temp_sold_1 - prices[i])
            sold_2 = max(temp_sold_2, temp_hold_2 + prices[i])

        return max(sold_1, sold_2)
