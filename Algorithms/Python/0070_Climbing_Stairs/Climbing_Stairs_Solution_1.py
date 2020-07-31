
# Space: O(n)
# Time: O(n)

# explanation: Recursion with Memoization

class Solution:
    def __init__(self):
        self.data = {}

    def climbStairs(self, n: int) -> int:

        if n in self.data: return self.data[n]
        if n <= 2: return n

        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.data[n] = res

        return self.data[n]




