
# Space: O(1)
# Time: O(n)


class Solution:
    def minOperations(self, nums, x):
        length = len(nums)
        if length == 1:
            return 1 if nums[0] == x else -1

        target_to_delete = sum(nums) - x
        length_of_target_to_delete = -1
        left = 0

        for right in range(length):
            target_to_delete -= nums[right]
            while target_to_delete < 0:
                target_to_delete += nums[left]
                left += 1

            if target_to_delete == 0:
                length_of_target_to_delete = max(length_of_target_to_delete, right - left + 1)

        return length - length_of_target_to_delete if length_of_target_to_delete != -1 else -1





