
# Space: O(1)
# Time: O(logn)

class Solution:
    def search(self, nums, target):
        length = len(nums)
        if length == 0: return False
        if length == 1: return True if nums[0] == target else False

        left, right = 0, length - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target: return True

            # handle duplicates
            if nums[mid] == nums[left]:
                left += 1
            elif nums[mid] == nums[right]:
                right -= 1

            elif nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[mid] < nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return True if nums[left] == target else False





