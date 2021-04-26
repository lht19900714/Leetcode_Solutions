
# Space: O(1)
# Time: O(n)

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1: return

        for x in range(n - 1):
            offset = 1
            for y in range(m - 2 - x, -1, -1):
                matrix[y][x], matrix[y + offset][x + offset] = matrix[y + offset][x + offset], matrix[y][x]
                offset += 1

        for y in range(m // 2):
            for x in range(n):
                matrix[y][x], matrix[m - y - 1][x] = matrix[m - y - 1][x], matrix[y][x]




