
# Space: O(n)
# Time: O(n)

import collections

class Solution:
    def majorityElement(self, nums):
        data = collections.Counter(nums)

        for k in data:
            if data[k] > len(nums) // 2:
                return k





