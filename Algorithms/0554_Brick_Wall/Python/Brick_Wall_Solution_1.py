
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def leastBricks(self, wall):
        height = len(wall)
        if height == 1:
            return 0 if len(wall[0]) > 1 else 1
        cache = []
        count = collections.defaultdict(int)
        res, final_res = -1, 0

        for row in wall:
            edge = []
            for i in range(1, len(row)):
                edge.append(sum(row[:i]))
            cache.append(edge)

        for row in cache:
            for e in row:
                count[e] += 1
                if res == -1:
                    res = e
                else:
                    res = e if count[e] > count[res] else res

        if res == -1: return height

        for row in cache:
            if res not in row:
                final_res += 1

        return final_res




