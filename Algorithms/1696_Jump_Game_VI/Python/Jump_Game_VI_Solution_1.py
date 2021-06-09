
# Space: O(n)
# Time: O(n)

class Solution:
    def maxResult(self, nums, k):
        length = len(nums)
        if length == 1: return nums[0]

        dp = [0 for _ in range(length)]
        queue = [0]
        dp[0] = nums[0]

        for i in range(1, length):
            dp[i] = nums[i] + dp[queue[0]]

            while queue and dp[i] >= queue[-1]:
                queue.pop()

            while queue and i - len(queue) >= k:
                queue.pop(0)

            queue.append(i)

        return dp[-1]






