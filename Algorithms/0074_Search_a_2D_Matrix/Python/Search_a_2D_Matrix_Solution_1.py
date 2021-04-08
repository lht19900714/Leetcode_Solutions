
# Space: O(1)
# Time: O(nlogn)


class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        y = len(matrix)
        if y == 0: return False
        x = len(matrix[0])
        if x == 0: return False
        if y == 1 and x == 1 and matrix[0][0] == target: return True

        # first, find the target row
        top_row_number, bottom_row_number = 0, y - 1
        while top_row_number + 1 < bottom_row_number:
            mid_row_number = (top_row_number + bottom_row_number) // 2
            if matrix[mid_row_number][-1] == target: return True

            if matrix[mid_row_number][-1] < target:
                top_row_number = mid_row_number + 1
            elif matrix[mid_row_number][-1] > target:
                bottom_row_number = mid_row_number

        if matrix[top_row_number][-1] >= target:
            target_row = top_row_number
        elif matrix[bottom_row_number][-1] >= target:
            target_row = bottom_row_number
        else:
            return False

        # second, find the target number
        left_x, right_x = 0, x - 1
        while left_x <= right_x:
            mid_x = (left_x + right_x) // 2
            if matrix[target_row][mid_x] == target: return True

            if matrix[target_row][mid_x] > target:
                right_x = mid_x - 1
            elif matrix[target_row][mid_x] < target:
                left_x = mid_x + 1
        return False





