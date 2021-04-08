
# Space: O(1)
# Time: O(n)

class Solution:
    def majorityElement(self, nums):
        length = len(nums)
        if length == 1: return nums

        majority = length // 3
        nums.sort()

        count = 0
        res = set()

        for i in range(length):
            if i == 0 or nums[i] == nums[i - 1]:
                count+=1
            elif nums[i] != nums[i - 1]:
                if count > majority:
                    res.add(nums[i - 1])
                count = 1

        if count > majority:
            res.add(nums[-1])

        return res







