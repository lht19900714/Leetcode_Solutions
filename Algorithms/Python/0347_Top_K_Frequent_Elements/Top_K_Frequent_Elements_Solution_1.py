
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def topKFrequent(self, nums, k):
        counts = collections.Counter(nums)
        res = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)[:k]
        return res

