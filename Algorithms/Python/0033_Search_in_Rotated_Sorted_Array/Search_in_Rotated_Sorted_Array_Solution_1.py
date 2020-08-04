
# Space: O(1)
# Time: O(logn)

class Solution:
    def search(self, nums, target):
        length = len(nums)
        if length == 0: return -1
        if length == 1: return 0 if nums[0] == target else -1

        # First, find out the actual end point of sorted array
        left, right = 0, length - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        actual_end_point = right if nums[right] > nums[left] else left

        # Second, execute regular binary search for target number
        res = self.binary_search(nums, target, 0, actual_end_point)
        if res != -1:
            return res
        else:
            return self.binary_search(nums, target, actual_end_point + 1, length - 1)

    def binary_search(self, alist, target, start, end):
        left, right = start, end
        while left <= right:
            mid = (left + right) // 2
            if alist[mid] == target:
                return mid
            if alist[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1



