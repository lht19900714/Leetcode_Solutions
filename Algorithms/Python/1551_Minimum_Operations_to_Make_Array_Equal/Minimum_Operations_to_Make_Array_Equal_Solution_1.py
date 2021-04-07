
# Space: O(1)
# Time: O(n)

class Solution:
    def minOperations(self, n):
        if n == 1: return 0
        res = 0
        if n % 2 == 0:
            mid_left = 2 * ((n // 2) - 1) + 1
            mid_right = 2 * (n // 2) + 1
            target_number = (mid_left + mid_right) // 2
        elif n % 2 != 0:
            target_number = 2 * (n // 2) + 1

        for i in range(1, target_number, 2):
            res += target_number - i

        return res





