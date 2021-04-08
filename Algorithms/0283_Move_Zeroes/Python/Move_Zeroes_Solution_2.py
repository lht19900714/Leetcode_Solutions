
# Space: O(1)
# Time: O(n)

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        temp = 0
        while n:
            if nums[temp] == 0:
                nums.append(nums.pop(temp))
            else:
                temp += 1
            n -= 1






