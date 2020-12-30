
# Space: O(1)
# Time: O(n)

class Solution:
    def gameOfLife(self, board):

        def count_live(x, y, n, m):
            direction = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [1, -1], [1, 1], [-1, 1]]
            live_count = 0
            for dir_y, dir_x in direction:
                temp_y, temp_x = y + dir_y, x + dir_x
                if 0 <= temp_y < m and 0 <= temp_x < n:
                    if board[temp_y][temp_x] == 1:
                        live_count += 1
            return live_count

        m = len(board)
        n = len(board[0])

        cache = []

        for y in range(m):
            for x in range(n):
                live_count = count_live(x, y, n, m)
                if board[y][x] == 1 and (live_count > 3 or live_count < 2):
                    cache.append([y, x])
                elif board[y][x] == 0 and live_count == 3:
                    cache.append([y, x])

        for y, x in cache:
            board[y][x] = 0 if board[y][x] == 1 else 1




