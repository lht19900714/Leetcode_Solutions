
# Space: O(1)
# Time: O(nlogn)

# Recursive approach

class Solution:
    def searchMatrix(self, matrix, target):
        y = len(matrix)
        if y == 0: return False
        x = len(matrix[0])
        if x == 0: return False

        def helper(matrix, x_left, x_right, y_left, y_right, target):
            if not 0 <= x_left <= x_right: return False
            if not 0 <= y_left <= y_right: return False

            mid_x = (x_left + x_right) // 2
            mid_y = (y_left + y_right) // 2

            mid = matrix[mid_y][mid_x]
            if mid == target: return True

            if mid < target:
                return helper(matrix, mid_x + 1, x_right, y_left, y_right, target) or helper(matrix, x_left, x_right, mid_y + 1, y_right, target)
            if mid > target:
                return helper(matrix, x_left, mid_x - 1, y_left, y_right, target) or helper(matrix, x_left, x_right, y_left, mid_y - 1, target)

        return helper(matrix, 0, x - 1, 0, y - 1, target)




