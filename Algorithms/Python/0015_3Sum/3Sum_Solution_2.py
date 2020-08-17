
# Space: O(1)
# Time: O(n^2)


class Solution:
    def threeSum(self, nums):

        nums.sort()
        length = len(nums)
        res = set()

        for i in range(length - 1):
            if i > 0 and nums[i] == nums[i - 1]: continue

            left, right = i + 1, length - 1

            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1

        return res





