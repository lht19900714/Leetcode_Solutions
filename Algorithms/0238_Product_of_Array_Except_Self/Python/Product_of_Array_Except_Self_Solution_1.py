
# Space: O(n)
# Time: O(n)

class Solution:
    def productExceptSelf(self, nums):
        list1 = [1 for _ in range(len(nums))]
        list2 = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            list1[i] = list1[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            list2[i] = list2[i + 1] * nums[i + 1]

        return [i * j for i, j in zip(list1, list2)]




