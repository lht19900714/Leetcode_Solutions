
# Space: O(n)
# Time: O(n)

# explanation:
#            transition function:
#            init: if i <= 2: dp[i] = i
#            function: dp[i] = dp[i - 1] + dp[i - 2]


class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2: return n

        # initial dp array to record result at each stair, add one extra space for better understanding.
        dp = [0] * (n + 1)

        for i in range(len(dp)):
            if i <= 2:
                dp[i] = i
            else:
                dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


