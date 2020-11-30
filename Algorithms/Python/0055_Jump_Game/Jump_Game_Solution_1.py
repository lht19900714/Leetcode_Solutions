
# Space: O(1)
# Time: O(n)


class Solution:
    def canJump(self, nums):
        length = len(nums)
        if length == 1: return True

        max_step = 0
        for i in range(length):
            if nums[i] == 0 and i != length - 1:
                if max_step <= i: return False
            max_step = max(max_step, i + nums[i])
        return True




