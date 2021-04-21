
# Space: O(n)
# Time: O(n)

class Solution:

    def minimumTotal(self, triangle):
        length = len(triangle)
        if length == 1: return sum(triangle[0])

        cache = {}
        for x in range(len(triangle[length - 1])):
            cache[(x, length - 1)] = triangle[length - 1][x]

        def dfs(board, x, y):
            if (x, y) in cache: return cache[(x, y)]

            res = triangle[y][x] + min(dfs(board, x, y + 1), dfs(board, x + 1, y + 1))

            cache[(x, y)] = res
            return res

        return dfs(triangle, 0, 0)




