
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def topKFrequent(self, words, k):
        data = collections.Counter(words)

        res = sorted(data.keys(), key=lambda x: (-data[x], x))

        return res[:k]




