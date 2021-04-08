
# Space: O(n)
# Time: O(n)

import collections


class Solution:

    def findMinHeightTrees2(self, n: int, edges):
        if n <= 2:
            return [i for i in range(n)]

        data = collections.defaultdict(list)
        for i, j in edges:
            data[i].append(j)
            data[j].append(i)

        remaining_node = n
        leaves = [i for i in range(n) if len(data[i]) == 1]

        while remaining_node > 2:
            remaining_node -= len(leaves)
            new_leaf = []
            while leaves:
                cur = leaves.pop()
                for i in data[cur]:
                    data[i].remove(cur)
                    if len(data[i]) == 1:
                        new_leaf.append(i)
            leaves = new_leaf

        return leaves




