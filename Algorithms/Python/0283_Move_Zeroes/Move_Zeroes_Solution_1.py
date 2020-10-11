
# Space: O(1)
# Time: O(n)

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 1: return

        slow, fast = 0, 0
        while fast < length and slow < length:

            if nums[slow] != 0:
                slow += 1
                if fast < slow: fast = slow

            elif nums[slow] == 0:
                while fast < length and nums[fast] == 0:
                    fast += 1

                # handle out of index issue
                if fast == length: fast = length - 1

                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1



