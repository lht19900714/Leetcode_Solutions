
# Space: O(n)
# Time: O(n)

import math


class Solution:
    def judgeSquareSum(self, c):
        if c <= 2: return True
        cache = [i for i in range(math.ceil(pow(c, 0.5)) + 1)]
        left, right = 0, len(cache)-1
        while left <= right:
            if pow(cache[left], 2) + pow(cache[right], 2) == c: return True
            if pow(cache[left], 2) + pow(cache[right], 2) < c:
                left += 1
            elif pow(cache[left], 2) + pow(cache[right], 2) > c:
                right -= 1
        return False




