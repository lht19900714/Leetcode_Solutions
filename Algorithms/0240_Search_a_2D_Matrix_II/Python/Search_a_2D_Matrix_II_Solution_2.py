
# Space: O(1)
# Time: O(n)

# Iterative approach

class Solution:
    def searchMatrix(self, matrix, target):
        y = len(matrix)
        if y == 0: return False
        x = len(matrix[0])
        if x == 0: return False

        # start point of searching(top left corner of the matrix)
        cur_x, cur_y = x - 1, 0

        while cur_x >= 0 and cur_y < y:
            if matrix[cur_y][cur_x] == target: return True

            # since we started from top left corner, the only way to get bigger number is moving to next row.
            if matrix[cur_y][cur_x] < target: cur_y += 1

            # since we started from top left corner, the only way to get smaller number is moving to previous column.
            elif matrix[cur_y][cur_x] > target: cur_x -= 1

        return False




