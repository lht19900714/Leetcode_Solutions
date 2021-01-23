
# Space: O(n)
# Time: O(n)

class Solution:
    def diagonalSort(self, mat):
        m = len(mat)
        if m == 0: return mat
        n = len(mat[0])

        def mySort(x, y):
            temp = []
            temp_x, temp_y = x, y
            while 0 <= temp_x < n and 0 <= temp_y < m:
                temp.append(mat[temp_y][temp_x])
                temp_x += 1
                temp_y += 1
            index = 0
            temp.sort()
            while 0 <= x < n and 0 <= y < m and index < len(temp):
                mat[y][x] = temp[index]
                x += 1
                y += 1
                index += 1

        for z in range(n):
            mySort(z, 0)

        for z in range(1, m):
            mySort(0, z)

        return mat





