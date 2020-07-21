
# Space: O(l)
# Time: O(m * n * l)

class Solution:
    def exist(self, board, word) -> bool:

        column_length = len(board)
        row_length = len(board[0])
        word_length = len(word)

        def dfs(x, y, index):
            if index >= word_length: return True
            if (not 0 <= x < row_length) or (not 0 <= y < column_length): return False
            if board[y][x] != word[index]: return False

            temp = board[y][x]
            board[y][x] = '*'

            if dfs(x - 1, y, index + 1): return True
            if dfs(x + 1, y, index + 1): return True
            if dfs(x, y - 1, index + 1): return True
            if dfs(x, y + 1, index + 1): return True

            board[y][x] = temp

        for column in range(column_length):
            for row in range(row_length):
                if dfs(row, column, 0): return True
        return False

