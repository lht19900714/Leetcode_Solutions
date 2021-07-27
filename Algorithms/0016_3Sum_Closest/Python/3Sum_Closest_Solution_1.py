
# Space: O(1)
# Time: O(n^2)

class Solution:
    def threeSumClosest(self, nums, target):
        length = len(nums)
        if length == 3: return sum(nums)
        nums = sorted(nums)
        res = sum(nums[:3])
        for i in range(length - 2):
            left, right = i + 1, length - 1
            while left < right:
                if abs((nums[i] + nums[left] + nums[right]) - target) < abs(res - target):
                    res = nums[i] + nums[left] + nums[right]
                if nums[i] + nums[left] + nums[right] == target: return res
                if nums[i] + nums[left] + nums[right] < target: left += 1
                if nums[i] + nums[left] + nums[right] > target: right -= 1

        return res




