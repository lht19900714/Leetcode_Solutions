
# Space: O(n)
# Time: O(n)

class Solution:
    def stoneGame(self, piles):
        length = len(piles)
        if length <= 2: return True

        cache = {}

        # flag==1: alex turn
        # flag==0: lee turn
        def dfs(left, right, nums, alex, lee, flag):
            if left > right: return alex > lee
            key = str(left) + ',' + str(right)
            if key in cache: return cache[key]

            if flag == 1:
                alex += nums[left]
                res = dfs(left + 1, right, nums, alex, lee, 0)
                cache[key] = res
                alex -= nums[left]
                if res: return res

                alex += nums[right]
                res = dfs(left, right - 1, nums, alex, lee, 0)
                cache[key] = res
                alex -= nums[right]
                if res: return res

            if flag == 0:
                lee += nums[left]
                res = dfs(left + 1, right, nums, alex, lee, 1)
                cache[key] = res
                lee -= nums[left]
                if res: return res

                lee += nums[right]
                res = dfs(left, right - 1, nums, alex, lee, 1)
                cache[key] = res
                lee -= nums[right]
                if res: return res

            return False

        return dfs(0, length - 1, piles, 0, 0, 1)





