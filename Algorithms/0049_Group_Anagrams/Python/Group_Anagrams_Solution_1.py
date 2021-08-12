
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def groupAnagrams(self, strs):
        length = len(strs)
        if length == 1: return [strs]
        res = []
        cache = collections.defaultdict(list)

        for word in strs:
            key = ''.join(sorted([c for c in word]))
            cache[key].append(word)

        for key in cache:
            res.append(cache[key])
        return res





