
# Space: O(1)
# Time: O(n)

# same approach as solution 2, compress space complexity from O(n) to O(1).

class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2: return n

        previous_1_step = 2
        previous_2_step = 1

        for i in range(3,n+1):
            res = previous_2_step + previous_1_step
            previous_2_step, previous_1_step = previous_1_step, res

        return res




