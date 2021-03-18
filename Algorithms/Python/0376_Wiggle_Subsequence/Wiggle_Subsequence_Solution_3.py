
# Space: O(1)
# Time: O(n)

class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) == 1: return 1
        if len(nums) == 2: return 1 if nums[0] == nums[1] else 2

        res = 1
        diff = nums[-1] - nums[-2]

        for i in range(len(nums)-2,-1,-1):
            if i == len(nums) - 2:
                res = 2 if diff != 0 else 1
            else:
                cur_diff = nums[i + 1] - nums[i]
                if (cur_diff > 0 and diff <= 0) or (cur_diff < 0 and diff >= 0):
                    res = res + 1
                    diff = cur_diff

        return res




