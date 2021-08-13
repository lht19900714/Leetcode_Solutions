
# Space: O(n)
# Time: O(n)

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0: return
        n = len(matrix[0])
        cache = []
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    cache.append([x, y])

        for x, y in cache:
            self.make_zero(x, y, m, n, matrix)

    def make_zero(self, x, y, m, n, matrix):
        index_x, index_y = 0, 0

        while index_x < n:
            matrix[y][index_x] = 0
            index_x += 1

        while index_y < m:
            matrix[index_y][x] = 0
            index_y += 1




