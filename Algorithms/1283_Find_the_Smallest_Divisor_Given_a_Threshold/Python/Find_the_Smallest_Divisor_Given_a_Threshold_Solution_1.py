
# Space: O(1)
# Time: O(logn)

import math

class Solution:
    def smallestDivisor(self, nums, threshold):
        length = len(nums)
        if length == 1: return round(nums[0] / threshold)

        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2

            if sum(map(lambda x: math.ceil(x / mid), nums)) <= threshold:
                right = mid
            else:
                left = mid + 1

        return left




