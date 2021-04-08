
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def wordSubsets(self, A, B):
        counter_B = collections.defaultdict(int)
        res = []
        for wordB in B:
            temp_counter = collections.Counter(wordB)
            for k, v in temp_counter.items():
                counter_B[k] = max(counter_B[k], v)

        for wordA in A:
            temp_counter_a = collections.Counter(wordA)
            for k, v in counter_B.items():
                if not (k in temp_counter_a and temp_counter_a[k] >= v):
                    break
            else:
                res.append(wordA)

        return res





