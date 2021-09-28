
# Space: O(1)
# Time: O(n)

class Solution:
    def sortArrayByParityII(self, nums):
        even, odd = 0, 1
        while even < len(nums) and odd < len(nums):
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 != 0:
                odd += 2
            else:
                nums[odd], nums[even] = nums[even], nums[odd]
                even += 2
                odd += 2
        return nums




