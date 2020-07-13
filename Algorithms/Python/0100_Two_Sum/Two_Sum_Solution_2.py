
# Space: O(n)
# Time: O(n)

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dict = {}
        for i in range(len(nums)):
            temp_target = target - nums[i]
            if temp_target in temp_dict and temp_dict[temp_target] != i:
                return [i, temp_dict[temp_target]]
            temp_dict[nums[i]] = i
