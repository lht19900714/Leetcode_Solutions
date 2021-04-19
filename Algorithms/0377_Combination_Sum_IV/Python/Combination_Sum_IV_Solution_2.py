
# Space: O(n)
# Time: O(n^2)

class Solution:
    def combinationSum4(self, nums, target):
        nums = sorted(nums)
        if nums[0] > target: return 0

        dp = [0 for _ in range(target + 1)]
        for num in nums:
            if num < len(dp):
                dp[num] = 1

        for i in range(1, len(dp)):
            for num in nums:
                if i + num <= target:
                    dp[i + num] += dp[i]

        return dp[-1]




