
# Space: O(1)
# Time: O(n)

class Solution:
    def checkPossibility(self, nums):
        length = len(nums)
        if length <= 1: return True
        slow, fast = -1, 0

        while fast < length - 1:
            if nums[fast] > nums[fast + 1]:
                if slow != -1: return False
                slow = fast
            fast += 1

        if slow in [-1, 0, length - 2]: return True
        if nums[slow - 1] <= nums[slow + 1]: return True
        if nums[slow] <= nums[slow + 2]: return True
        return False




