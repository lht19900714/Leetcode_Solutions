
# Space: O(1)
# Time: O(n^2)


class Solution:
    def threeSum(self, nums):

        nums.sort()
        length = len(nums)
        res = set()

        for i in range(length - 1):
            left = 0
            right = length - 1

            while left < i < right:
                if nums[left] + nums[i] + nums[right] == 0:
                    res.add((nums[left], nums[i], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[i] + nums[right] > 0:
                    right -= 1
                elif nums[left] + nums[i] + nums[right] < 0:
                    left += 1

        return res



