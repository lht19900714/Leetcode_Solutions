
# Space: O(n)
# Time: O(n)

import collections

class Solution:
    def advantageCount(self, A, B):
        length = len(A)
        if length <= 1: return A

        sortedA, sortedB = sorted(A), sorted(B)
        cache = collections.defaultdict(list)
        res = []
        remaining = []
        index = 0

        for a in sortedA:
            if a > sortedB[index]:
                cache[sortedB[index]].append(a)
                index += 1
            else:
                remaining.append(a)

        for b in B:
            if cache[b]:
                res.append(cache[b].pop())
            else:
                res.append(remaining.pop())

        return res




