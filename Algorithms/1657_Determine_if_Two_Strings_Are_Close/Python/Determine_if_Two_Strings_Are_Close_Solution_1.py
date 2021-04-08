
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        length_1, length_2 = len(word1), len(word2)

        if length_1 != length_2: return False

        counter_1, counter_2 = collections.Counter(word1), collections.Counter(word2)

        if set(counter_1.keys()) != set(counter_2.keys()): return False

        if sorted(counter_1.values()) != sorted(counter_2.values()): return False

        return True





