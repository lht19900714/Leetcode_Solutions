

# Space: O(1)
# Time: O(n)


class Solution:
    def maxArea(self, height):
        length = len(height)
        if length == 2: return min(height[0], height[1]) * 1

        res = 0
        left, right = 0, length - 1

        while left != right:
            res = max(res, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res




