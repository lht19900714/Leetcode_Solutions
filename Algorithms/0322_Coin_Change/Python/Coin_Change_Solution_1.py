
# Space: O(1)
# Time: O(n^2)

class Solution:
    def coinChange(self, coins, amount):
        if amount == 0: return 0
        if len(coins) == 0: return -1
        coins.sort(reverse=True)
        self.res = amount + 1

        def dfs(cur_amount, cur_index, cur_res):
            if cur_amount == 0:
                self.res = min(self.res, cur_res)
                return
            if cur_index == len(coins):
                return
            cur_coin = coins[cur_index]

            for count in range(cur_amount // cur_coin, -1, -1):
                if count + cur_res >= self.res: break
                dfs(cur_amount - cur_coin * count, cur_index + 1, cur_res + count)

        dfs(amount, 0, 0)

        return self.res if self.res != amount + 1 else -1





