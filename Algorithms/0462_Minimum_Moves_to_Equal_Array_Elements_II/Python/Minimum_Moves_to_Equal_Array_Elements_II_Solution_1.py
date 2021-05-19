
# Space: O(1)
# Time: O(n)

class Solution:

    def minMoves2(self, nums):
        length = len(nums)
        if length <= 1: return 0
        res = 0
        nums = sorted(nums)
        mid = length // 2

        for i in range(length):
            res += abs(nums[i] - nums[mid])

        return res




