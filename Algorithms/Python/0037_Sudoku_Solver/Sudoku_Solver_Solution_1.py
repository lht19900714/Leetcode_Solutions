
# Space: O(n)
# Time: O(n)

class Solution:
    def solveSudoku(self, board):

        self.positions = []
        self.flag = 'N'

        for y in range(9):
            for x in range(9):
                if board[y][x] == '.':
                    self.positions.append([y, x])

        def backtracking(board, positions):
            if len(positions) == 0:
                self.flag = 'Y'
                return
            cur_y, cur_x = positions[-1]
            for num in range(1, 10):
                if self.check_number(board, cur_x, cur_y, str(num)):
                    temp = positions.pop()
                    board[cur_y][cur_x] = str(num)
                    backtracking(board, positions)
                    if self.flag != 'N': return
                    board[cur_y][cur_x] = '.'
                    positions.append(temp)

        backtracking(board, self.positions)

    def check_number(self, board, x, y, value):

        # check row
        if value in board[y]: return False

        # check column
        for i in range(9):
            if board[i][x] == value: return False


        # check box

        # confirm searching area
        index = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        x_range, y_range = [], []
        for i in range(3):
            if x in index[i]: x_range = index[i]
            if y in index[i]: y_range = index[i]

        for temp_y in y_range:
            for temp_x in x_range:
                if board[temp_y][temp_x] == value: return False

        return True




