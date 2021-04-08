
# Space: O(1)
# Time: O(n)

class Solution:
    def largestRectangleArea(self, heights):
        length = len(heights)
        if length == 0: return 0

        res = 0
        stack = []

        for i in range(length):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                temp = stack.pop()

                if len(stack) == 0:
                    width = i
                else:
                    width = i - stack[-1] - 1

                res = max(res, heights[temp] * width)

            stack.append(i)

        while stack:
            temp = stack.pop()

            if len(stack) == 0:
                width = length
            else:
                width = length - stack[-1] - 1

            res = max(res, heights[temp] * width)

        return res






