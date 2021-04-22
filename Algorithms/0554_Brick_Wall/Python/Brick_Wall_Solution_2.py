
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def leastBricks(self, wall):
        height = len(wall)
        if height == 1:
            return 0 if len(wall[0]) > 1 else 1
        cache, max_edge = collections.defaultdict(int), 0

        for row in wall:
            for i in range(1, len(row)):
                edge = sum(row[:i])
                cache[edge] += 1
                max_edge = max(max_edge, cache[edge])

        return height - max_edge




