
# Space: O(n)
# Time: O(n)

# better code than solution 1

class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) == 1: return 1
        if len(nums) == 2: return 1 if nums[0] == nums[1] else 2

        dp = [1 for _ in range(len(nums))]
        diff = nums[-1] - nums[-2]

        for i in range(len(nums) - 2, -1, -1):
            if i == len(nums) - 2:
                dp[i] = 2 if diff != 0 else 1
            else:
                cur_diff = nums[i + 1] - nums[i]
                if (cur_diff > 0 and diff <= 0) or (cur_diff < 0 and diff >= 0):
                    dp[i] = dp[i + 1] + 1
                    diff = cur_diff
                else:
                    dp[i] = dp[i + 1]

        return dp[0]




