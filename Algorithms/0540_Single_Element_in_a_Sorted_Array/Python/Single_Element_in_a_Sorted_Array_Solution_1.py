# Space: O(1)
# Time: O(logn)


class Solution:
    def singleNonDuplicate(self, nums):
        length = len(nums)
        if length == 0: return
        if length == 1: return nums[0]
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            mid_pair = mid + 1 if mid % 2 == 0 else mid - 1
            if nums[mid] == nums[mid_pair]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


             

