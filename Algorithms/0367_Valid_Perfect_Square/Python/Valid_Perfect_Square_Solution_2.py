
# Space: O(1)
# Time: O(logn)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num: return True

            if mid * mid < num:
                left = mid + 1
            elif mid * mid > num:
                right = mid - 1

        return False





