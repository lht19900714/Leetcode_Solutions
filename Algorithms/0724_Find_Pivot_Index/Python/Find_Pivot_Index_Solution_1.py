
# Space: O(1)
# Time: O(n^2)

class Solution:
    def pivotIndex(self, nums):
        length = len(nums)
        if length <= 1: return -1

        for i in range(length):
            if i == 0:
                if sum(nums[i + 1:]) == 0:
                    return i
            elif i == length - 1:
                if sum(nums[:i]) == 0:
                    return i
            elif sum(nums[:i]) == sum(nums[i + 1:]):
                return i

        return -1



