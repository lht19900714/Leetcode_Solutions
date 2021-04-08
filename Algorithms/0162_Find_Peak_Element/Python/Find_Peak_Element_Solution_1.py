
# Space: O(1)
# Time: O(n)

class Solution:
    def findPeakElement(self, nums):
        length = len(nums)
        if length <= 1: return 0
        if length == 2:
            return 0 if nums[0] > nums[1] else 1

        first, second, third = 0, 1, 2
        while third < length:
            if nums[first] < nums[second] > nums[third]:
                return second
            elif nums[first] > nums[second] and first == 0:
                return first
            elif nums[second] < nums[third] and third == length - 1:
                return third
            first += 1
            second += 1
            third += 1



