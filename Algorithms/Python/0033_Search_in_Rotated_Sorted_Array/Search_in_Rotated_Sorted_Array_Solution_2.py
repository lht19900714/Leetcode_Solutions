
# Space: O(1)
# Time: O(logn)

class Solution:
    def search(self, nums, target):
        length = len(nums)
        if length == 0: return False
        if length == 1: return 0 if nums[0] == target else -1

        left, right = 0, length

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid

            # if target and nums[mid] are in the same region, execute regular binary search
            if (nums[left] <= nums[mid] and nums[left] <= target) or (nums[mid] < nums[left] and target < nums[left]):
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid

            # if target and nums[mid] aren't in the same section, modify search region
            elif target >= nums[0]:
                right = mid
            elif target < nums[0]:
                left = mid + 1

        return -1





