
# Space: O(1)
# Time: O(n)

class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        if length <= 1: return 0

        res = 0
        lowest_price = prices[0]

        for i in range(length):
            lowest_price = min(lowest_price, prices[i])
            res = max(res, prices[i] - lowest_price)

        return res
