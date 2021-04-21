
# Space: O(n)
# Time: O(n)

class Solution:

    def minimumTotal(self, triangle):
        length = len(triangle)
        if length == 1: return sum(triangle[0])

        cache = {}
        for x in range(len(triangle[length - 1])):
            cache[(x, length - 1,)] = triangle[length - 1][x]

        for y in range(length - 2, -1, -1):
            for x in range(len(triangle[y])):
                cache[(x, y)] = min(cache[(x, y + 1)], cache[(x + 1, y + 1)]) + triangle[y][x]

        return cache[(0,0)]




