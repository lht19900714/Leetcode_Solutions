
# Space: O(n)
# Time: O(n)

class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) == 1: return 1
        if len(nums) == 2: return 1 if nums[0] == nums[1] else 2

        dp = [1 for _ in range(len(nums))]
        difference = nums[-1] - nums[-2]

        for i in range(len(nums) - 2, -1, -1):
            if i == len(nums) - 2:
                if nums[i] != nums[i + 1]:
                    difference = nums[i + 1] - nums[i]
                    dp[i] = dp[i + 1] + 1

            elif nums[i] == nums[i + 1]:
                dp[i] = dp[i + 1]

            elif difference == 0:
                difference = nums[i + 1] - nums[i]
                dp[i] = dp[i + 1] + 1

            elif (nums[i + 1] - nums[i]) * difference < 0:
                difference = nums[i + 1] - nums[i]
                dp[i] = dp[i + 1] + 1

            elif (nums[i + 1] - nums[i]) * difference >= 0:
                dp[i] = dp[i + 1]

        return dp[0]




