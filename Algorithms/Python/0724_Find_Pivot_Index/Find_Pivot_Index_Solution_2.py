
# Space: O(n)
# Time: O(n)

class Solution:
    def pivotIndex(self, nums):
        length = len(nums)
        if length <= 1: return -1

        left_sum = [0] * length
        right_sum = [0] * length

        # calculate left sum for each index
        for i in range(1, length):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]
        # calculate right sum for each index
        for i in range(length - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]

        index = 0
        for left, right in zip(left_sum, right_sum):
            if left == right:
                return index
            index += 1

        return -1




