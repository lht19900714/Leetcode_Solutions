
# Space: O(n)
# Time: O(n)

class Solution:
    def findUnsortedSubarray(self, nums):
        length = len(nums)
        if length <= 1: return 0
        stack = []
        left, right = length - 1, 0

        for i in range(length):
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)

        if left == length - 1: return 0

        stack = []
        for j in range(length - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[j]:
                right = max(right, stack.pop())
            stack.append(j)

        return right - left + 1




