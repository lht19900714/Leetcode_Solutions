
# Space: O(1)
# Time: O(n)

class Solution:
    def removeElement(self, nums, val) -> int:

        length = len(nums)
        if length == 1:
            if nums[0] == val: return 0
            if nums[0] != val: return 1

        slow = 0

        for i in range(length):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1

        return slow




