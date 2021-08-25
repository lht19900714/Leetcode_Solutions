
# Space: O(n)
# Time: O(n)

class Solution:
    def isValidSudoku(self, board) -> bool:

        # check row
        if not self.check_line(board, 0): return False

        # check column
        if not self.check_line(board, 1): return False

        # check box
        start_point = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        for y, x in start_point:
            if not self.check_box(board, x, y): return False

        return True

    def check_line(self, board, flag):
        if flag == 0:  # check row
            for y in range(9):
                cache = set()
                for x in range(9):
                    if board[y][x] == '.':
                        continue
                    elif board[y][x] not in cache:
                        cache.add(board[y][x])
                    else:
                        return False

        else:  # check column
            for x in range(9):
                cache = set()
                for y in range(9):
                    if board[y][x] == '.':
                        continue
                    elif board[y][x] not in cache:
                        cache.add(board[y][x])
                    else:
                        return False
        return True

    def check_box(self, board, x_start, y_start):
        cache = set()
        for y in range(y_start, y_start + 3):
            for x in range(x_start, x_start + 3):
                if board[y][x] == '.':
                    continue
                elif board[y][x] not in cache:
                    cache.add(board[y][x])
                else:
                    return False
        return True




