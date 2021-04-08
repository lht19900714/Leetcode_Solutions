
# Space: O(n)
# Time: O(n)


class Solution:
    def numberOfArithmeticSlices(self, A):
        length = len(A)
        if length < 3: return 0
        dp = [0 for _ in range(length)]
        res = 0

        for i in range(2, length):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
                res += dp[i]

        return res




                        
