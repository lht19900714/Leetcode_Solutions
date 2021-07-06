
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def minSetSize(self, arr):
        length = len(arr)
        counter = collections.Counter(arr)
        cache = sorted(list(set(arr)), key=lambda x: -counter[x])
        res, res_counter = length, 0

        for i in cache:
            res -= counter[i]
            res_counter += 1
            if res <= length // 2: return res_counter
        return res_counter




