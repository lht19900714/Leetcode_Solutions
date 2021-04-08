
# Space: O(1)
# Time: O(n)

class Solution:
    def rob(self, nums):
        length = len(nums)
        if length == 0: return 0
        if length == 1: return nums[0]
        if length == 2: return max(nums[0], nums[1])

        def helper(nums):
            length = len(nums)
            if length == 0: return 0
            if length == 1: return nums[0]
            if length == 2: return max(nums[0], nums[1])

            res = 0
            day_before_previous_day = nums[0]
            previous_day = max(nums[0], nums[1])

            for i in range(2, length):
                res = max(day_before_previous_day + nums[i], previous_day)
                day_before_previous_day = previous_day
                previous_day = res

            return res

        return max(helper(nums[:-1]), helper(nums[1:]))








