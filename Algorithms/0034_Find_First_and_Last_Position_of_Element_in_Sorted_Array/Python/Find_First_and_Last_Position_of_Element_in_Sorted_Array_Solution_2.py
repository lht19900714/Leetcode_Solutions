
# Space: O(1)
# Time: O(logn)

class Solution:
    def searchRange(self, nums, target):
        length = len(nums)
        if length == 0: return [-1, -1]
        if length == 1:
            return [0, 0] if nums[0] == target else [-1, -1]

        res = []
        left, right = 0, length
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        if left != length and nums[left] == target:
            res.append(left)
        else:
            return [-1, -1]

        left, right = 0, length
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        res.append(left - 1)

        return res




