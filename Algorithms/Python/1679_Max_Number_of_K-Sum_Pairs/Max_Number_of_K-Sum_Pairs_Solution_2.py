
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def maxOperations(self, nums, k):
        length = len(nums)
        if length == 1: return 0
        if length == 2: return 1 if sum(nums) == k else 0

        counter = collections.Counter(nums)
        res = 0

        for key in counter:
            res += min(counter[key], counter[k - key])

        return res // 2




                                                                                                                                           