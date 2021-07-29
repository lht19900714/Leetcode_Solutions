
# Space: O(1)
# Time: O(n)

class Solution:
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        if m == 1 and n == 1: return mat

        for y in range(m):
            for x in range(n):
                if mat[y][x] != 0:
                    left = mat[y][x - 1] if x - 1 >= 0 else float('inf')
                    top = mat[y - 1][x] if y - 1 >= 0 else float('inf')
                    mat[y][x] = min(top, left) + 1

        for y in range(m - 1, -1, -1):
            for x in range(n - 1, -1, -1):
                if mat[y][x] != 0:
                    right = mat[y][x + 1] if x + 1 < n else float('inf')
                    bottom = mat[y + 1][x] if y + 1 < m else float('inf')
                    mat[y][x] = min(right + 1, bottom + 1, mat[y][x])
        return mat




