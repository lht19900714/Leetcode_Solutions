
# Space: O(n)
# Time: O(n)


class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        if length <= 1:
            return 0

        # initial result array for first sell and second sell
        res_1, res_2 = [0] * length, [0] * length

        # get best sell result for "first sell", this approach same as Q.121
        min_price = prices[0]
        for i in range(1, length):
            min_price = min(min_price, prices[i])
            res_1[i] = max(res_1[i - 1], prices[i] - min_price)

        # get best sell result for "second sell".
        # similar approach from above, we iterate prices from end to front, and continuously maintain max_price.
        # so, the best sell result is max(res_2[i+1], max_price - prices[i])
        max_price = prices[-1]
        for i in range(length - 2, -1, -1):
            max_price = max(max_price, prices[i])
            res_2[i] = max(res_2[i + 1], max_price - prices[i])

        res = 0
        for first_result, second_result in zip(res_1, res_2):
            res = max(res, first_result + second_result)

        return res




