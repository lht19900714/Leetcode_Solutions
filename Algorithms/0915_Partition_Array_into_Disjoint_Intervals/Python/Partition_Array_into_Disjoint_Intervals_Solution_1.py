
# Space: O(n)
# Time: O(n)

class Solution:
    def partitionDisjoint(self, nums):
        length = len(nums)
        if length == 2: return 1
        left_max, right_min = [-1 for _ in range(length)], [-1 for _ in range(length)]
        left_max[0] = nums[0]
        right_min[-1] = nums[-1]

        for i in range(1, length):
            left_max[i] = max(nums[i], left_max[i - 1])

        for i in range(length - 2, -1, -1):
            right_min[i] = min(nums[i], right_min[i + 1])

        for i in range(length - 1):
            if left_max[i] <= right_min[i + 1]: return i + 1

        return -1




