
# Space: O(1)
# Time: O(n)

class Solution:
    def maxProduct(self, nums):
        if len(nums) == 1: return nums[0]

        current_max = nums[0]
        current_min = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            temp = current_max

            current_max = max(current_max * nums[i], current_min * nums[i], nums[i])
            current_min = min(temp * nums[i], current_min * nums[i], nums[i])

            res = max(current_max,res)

        return res







