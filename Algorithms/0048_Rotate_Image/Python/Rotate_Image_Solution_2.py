
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

        index = 0
        first, last = 0, n - 1
        while first < last:
            temp = last - first
            for i in range(temp):
                self.swap(matrix, first, first + i, first + i, last)
                self.swap(matrix, first, first + i, last, last - i)
                self.swap(matrix, first, first + i, last - i, first)
            first += 1
            last -= 1

    def swap(self, matrix, y1, x1, y2, x2):
        matrix[y1][x1], matrix[y2][x2] = matrix[y2][x2], matrix[y1][x1]




