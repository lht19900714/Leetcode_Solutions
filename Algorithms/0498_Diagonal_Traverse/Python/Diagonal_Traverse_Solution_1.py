
# Space: O(n)
# Time: O(n)


class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]: return []

        m, n = len(matrix), len(matrix[0])
        res = []

        # the total diagonal rows is m+n-1
        for each_diagonal_row in range(m + n - 1):
            temp = []

            # determine the "head" of each diagonal row
            if each_diagonal_row < n:
                y = 0
                x = each_diagonal_row
            else:
                y = each_diagonal_row - n + 1
                x = n - 1

            while 0 <= x < n and 0 <= y < m:
                temp.append(matrix[y][x])
                x -= 1
                y += 1

            res += (temp[::-1] if each_diagonal_row % 2 == 0 else temp[:])

        return res






