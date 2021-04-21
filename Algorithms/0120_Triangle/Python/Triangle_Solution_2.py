
# Space: O(n)
# Time: O(n)

class Solution:

    def minimumTotal(self, triangle):
        length = len(triangle)
        if length == 1: return sum(triangle[0])
        cache = triangle[-1]

        for y in range(length - 2, -1, -1):
            for x in range(y+1):
                cache[x] = min(cache[x], cache[x + 1]) + triangle[y][x]

        return cache[0]




