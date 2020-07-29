
# Space: O(1)
# Time: O(logn)

class Solution:
    def searchRange(self, nums, target):
        def find_first(nums, target):
            left = 0
            right = len(nums) - 1

            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            return -1

        def find_last(nums, target):
            left = 0
            right = len(nums) - 1

            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left
            return -1

        if len(nums) == 0: return [-1, -1]
        return [find_first(nums, target), find_last(nums, target)]




