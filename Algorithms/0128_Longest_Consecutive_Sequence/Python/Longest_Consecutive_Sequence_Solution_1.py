
# Space: O(n)
# Time: O(n)

class Solution:
    def longestConsecutive(self, nums):
        if not nums: return 0
        nums = sorted(list(set(nums)))
        res = 0
        counter = 1
        index = 1
        while index < len(nums):
            if nums[index] == nums[index - 1] + 1:
                counter += 1
            else:
                res = max(res, counter)
                counter = 1
            index += 1

        return max(res, counter)




