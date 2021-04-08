
# Space: O(1)
# Time: O(logn)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x

        left, right = 1, x - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if pow(mid, 2) == x: return mid

            if pow(mid, 2) < x:
                left = mid
            elif pow(mid, 2) > x:
                right = mid

        return right if pow(right, 2) < x else left



