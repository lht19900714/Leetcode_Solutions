
# Space: O(1)
# Time: O(n)

class NumMatrix:

    def __init__(self, matrix):
        self.board = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for y in range(row1, row2 + 1):
            for x in range(col1, col2 + 1):
                res += self.board[y][x]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)




