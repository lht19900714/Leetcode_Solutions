
# Space: O(1)
# Time: O(n)

class Solution:
    def removeDuplicates(self, nums) -> int:
        length = len(nums)
        if length == 1: return 1

        slow, fast = 0, 1

        while fast < length:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1






