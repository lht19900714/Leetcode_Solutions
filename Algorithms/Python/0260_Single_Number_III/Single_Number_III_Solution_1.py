
# Space: O(1)
# Time: O(n^2)

class Solution:
    def singleNumber(self, nums):
        return [i for i in nums if nums.count(i) == 1]



