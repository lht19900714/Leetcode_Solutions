
# Space: O(1)
# Time: O(n)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        for i in range(1, num):
            if i * i == num: return True
            if i * i > num: return False
        return False




