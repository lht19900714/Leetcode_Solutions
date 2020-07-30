
# Space: O(1)
# Time: O(n)

# same approach as solution 1, compress space complexity from O(n) to O(1).

class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        if length <= 1: return 0

        # initial three variable to record "yesterday" status.
        prev_cooldown, prev_sell, prev_hold = 0, 0, -float('inf')

        for i in range(length):

            hold = max(prev_hold, prev_cooldown - prices[i])
            sell = prev_hold + prices[i]
            cooldown = max(prev_cooldown, prev_sell)

            prev_hold, prev_sell, prev_cooldown = hold, sell, cooldown

        return max(sell, cooldown)




