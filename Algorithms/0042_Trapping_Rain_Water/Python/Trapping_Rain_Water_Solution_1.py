
# Space: O(1)
# Time: O(n)

class Solution:
    def trap(self, height) -> int:
        length = len(height)
        if length <= 2: return 0

        # find the highest_bar
        highest_bar = 0
        highest_bar_index = 0
        for i in range(length):
            if height[i] > highest_bar:
                highest_bar = height[i]
                highest_bar_index = i

        res = 0

        # calculate the water from left to highest_bar
        pointer_from_left = 0
        highest_bar_from_left = 0
        while pointer_from_left != highest_bar_index:
            highest_bar_from_left = max(highest_bar_from_left, height[pointer_from_left])
            res += highest_bar_from_left - height[pointer_from_left]
            pointer_from_left += 1

        # calculate the water from right to highest_bar
        pointer_from_right = length - 1
        highest_bar_from_right = 0
        while pointer_from_right != highest_bar_index:
            highest_bar_from_right = max(highest_bar_from_right, height[pointer_from_right])
            res += highest_bar_from_right - height[pointer_from_right]
            pointer_from_right -= 1

        return res



