
# Space: O(n)
# Time: O(n)

class Solution:
    def mostCompetitive(self, nums, k):
        if k == 1: return [min(nums)]

        stack = []

        for i in range(len(nums)):
            number_left = len(nums) - i
            while stack and stack[-1] > nums[i] and number_left > k - len(stack):
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])

        return stack




