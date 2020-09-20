
# Space: O(1)
# Time: O(n)

class Solution:
    def largestRectangleArea(self, heights):
        length = len(heights)
        if length == 0: return 0

        stack = []
        heights = [0] + heights + [0]
        res = 0

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:
                temp = stack.pop()
                width = i - stack[-1] - 1
                res = max(res, heights[temp] * width)

            stack.append(i)

        return res




