
# Space: O(1)
# Time: O(logn)

class Solution:
    def findPeakElement(self, nums):
        length = len(nums)
        if length <= 1: return 0
        if length == 2:
            return 0 if nums[0] > nums[1] else 1

        left, right = 0, length - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1]:
                left = mid
            else:
                right = mid
        if nums[left] > nums[right]:
            return left
        else:
            return right



