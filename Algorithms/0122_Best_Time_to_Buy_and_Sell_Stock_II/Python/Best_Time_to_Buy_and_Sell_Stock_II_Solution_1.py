
# Space: O(1)
# Time: O(n)

class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        if length <= 1: return 0

        res = 0
        cur = 0
        bottom, top = 0, 0
        while cur < length - 1:
            # looking for next valley
            while cur < length - 1 and prices[cur] >= prices[cur + 1]:
                cur += 1
            bottom = prices[cur]

            # looking for next perk
            while cur < length - 1 and prices[cur] < prices[cur + 1]:
                cur += 1
            top = prices[cur]

            res += top - bottom

        return res
