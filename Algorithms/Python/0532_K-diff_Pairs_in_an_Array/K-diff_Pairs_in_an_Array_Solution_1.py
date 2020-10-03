
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def findPairs(self, nums, k):
        temp_data = collections.Counter(nums)
        res = 0
        if k == 0:
            for i in temp_data:
                if temp_data[i] >= 2: res += 1
            return res

        for i in temp_data:
            if i + k in temp_data: res += 1

        return res





