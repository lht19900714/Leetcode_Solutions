
# Space: O(1)
# Time: O(nlogn)

class Solution:
    def maxOperations(self, nums, k):
        length = len(nums)
        if length == 1: return 0
        if length == 2: return 1 if sum(nums) == k else 0

        nums.sort()
        res = 0
        left, right = 0, length - 1

        while nums and left < right:
            if nums[left] + nums[right] == k:
                res += 1
                nums.pop(right)
                nums.pop(left)
                if not nums: return res
                left = left - 1 if left > 0 else left
                right = len(nums) - 1 if right >= len(nums) else right
            elif nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1

        return res




