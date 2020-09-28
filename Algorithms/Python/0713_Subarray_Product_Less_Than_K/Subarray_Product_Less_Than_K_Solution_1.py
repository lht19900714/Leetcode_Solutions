
# Space: O(1)
# Time: O(n)

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        length = len(nums)
        if length == 1 and nums[0] < k:
            return 1

        res, temp_num = 0, 1
        fast = 0
        for slow in range(length):

            if slow > fast:
                fast = slow
                temp_num = 1

            while fast < length and temp_num * nums[fast] < k:
                temp_num *= nums[fast]
                fast += 1

            res += (fast - slow)
            temp_num /= nums[slow]

        return res





