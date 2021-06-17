
# Space: O(1)
# Time: O(n)

class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):
        length = len(nums)
        if length == 1:
            return 1 if left <= nums[0] <= right else 0

        fast, slow, count, res = 0, 0, 0, 0
        while fast < length:
            if left <= nums[fast] <= right:
                count = fast - slow + 1
                res += count
            elif nums[fast] < left:
                res += count
            elif nums[fast] > right:
                slow = fast + 1
                count = 0
            fast += 1
        return res




