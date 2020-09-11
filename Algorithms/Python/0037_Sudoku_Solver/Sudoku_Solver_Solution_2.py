# Space: O(n)
# Time: O(n)

class Solution:
    def solveSudoku(self, board):
        self.row_status = [[0 for _ in range(9)] for _ in range(9)]
        self.column_status = [[0 for _ in range(9)] for _ in range(9)]
        self.box_status = [[0 for _ in range(9)] for _ in range(9)]

        for y in range(9):
            for x in range(9):

                # split whole board into 9 pieces, and assign index to each of them
                # top_left: 0 top: 1 top_right: 2
                # mid_left: 3 mid: 4 mid_right: 5
                # bot_left: 6 bot: 7 bot_right: 8
                box_index = (y // 3) * 3 + (x // 3)

                if board[y][x] != '.':
                    self.row_status[y][int(board[y][x]) - 1] = 1
                    self.column_status[x][int(board[y][x]) - 1] = 1
                    self.box_status[box_index][int(board[y][x]) - 1] = 1

        def backtracking(board, x, y):
            if y == 9: return True

            next_x = (x + 1) % 9
            next_y = y + 1 if next_x == 0 else y

            if board[y][x] != '.': return backtracking(board, next_x, next_y)

            for num in range(1, 10):
                box_index = (y // 3) * 3 + (x // 3)
                if self.row_status[y][num - 1] == 0 and self.column_status[x][num - 1] == 0 and self.box_status[box_index][num - 1] == 0:
                    self.row_status[y][num - 1] = 1
                    self.column_status[x][num - 1] = 1
                    self.box_status[box_index][num - 1] = 1
                    board[y][x] = str(num)
                    if backtracking(board, next_x, next_y): return True
                    board[y][x] = '.'
                    self.box_status[box_index][num - 1] = 0
                    self.column_status[x][num - 1] = 0
                    self.row_status[y][num - 1] = 0
            return False

        backtracking(board, 0, 0)




