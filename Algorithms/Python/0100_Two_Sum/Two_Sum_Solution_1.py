
# Space: O(n)
# Time: O(n)

import collections

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dict = collections.defaultdict(list)
        for i in range(len(nums)):
            temp_dict[nums[i]].append(i)

        for j in range(len(nums)):
            temp_target = target - nums[j]
            if temp_target in temp_dict:
                for z in temp_dict[temp_target]:
                    if z != j:
                        return [z, j]
