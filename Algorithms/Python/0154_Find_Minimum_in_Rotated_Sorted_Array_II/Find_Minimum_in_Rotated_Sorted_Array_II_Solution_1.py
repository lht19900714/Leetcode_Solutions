
# Space: O(1)
# Time: O(logn)

class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                right -= 1
        return nums[left] if nums[left] < nums[right] else nums[right]



