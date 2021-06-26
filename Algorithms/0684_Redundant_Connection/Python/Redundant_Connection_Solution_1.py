
# Space: O(n)
# Time: O(n)

import collections

class Solution:
    def findRedundantConnection(self, edges):
        cache = collections.defaultdict(set)
        res = None

        def dfs(start, end, visited):
            if start == end: return True
            if start in visited: return False
            visited.add(start)

            for i in cache[start]:
                if dfs(i, end, visited): return True
            return False

        for i, j in edges:
            if dfs(i, j, set()):
                res = [i, j]
            else:
                cache[i].add(j)
                cache[j].add(i)

        return res




