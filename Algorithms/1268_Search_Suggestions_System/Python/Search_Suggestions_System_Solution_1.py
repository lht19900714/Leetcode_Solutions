
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def suggestedProducts(self, products, searchWord):
        cache = collections.defaultdict(list)
        res = []
        for word in products:
            for i in range(1, len(word) + 1):
                cache[word[:i]].append(word)

        for i in range(1, len(searchWord) + 1):
            if searchWord[:i] in cache:
                res.append(sorted(cache[searchWord[:i]])[:3])
            else:
                res.append([])

        return res





