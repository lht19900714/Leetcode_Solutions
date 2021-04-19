
# Space: O(n)
# Time: O(n)

class Solution:
    def combinationSum4(self, nums, target):
        cache = {}

        def dfs(nums, target):
            if target < 0: return 0
            if target == 0: return 1
            if cache.get(target, -1) != -1: return cache[target]

            count = 0
            for num in nums:
                temp_target = target - num
                count += dfs(nums, temp_target)
            cache[target] = count

            return count

        dfs(nums, target)

        return cache[target]




