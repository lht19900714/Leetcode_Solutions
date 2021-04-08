
# Space: O(1)
# Time: O(n)

class Solution:
    def generateMatrix(self, n):
        if n == 1: return [[1]]

        # create board
        board = [[None for _ in range(n)] for _ in range(n)]

        # cursor moving direction [x,y]
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # point to current using direction
        direction_index = 0

        # initial cursor
        x, y, = 0, 0

        counter = 1

        while counter <= n * n:
            board[y][x] = counter
            counter += 1

            next_x = x + direction[direction_index][0]
            next_y = y + direction[direction_index][1]

            if 0 <= next_x < n and 0 <= next_y < n and board[next_y][next_x] is None:
                x = next_x
                y = next_y
            else:
                direction_index = (direction_index + 1) % len(direction)
                x = direction[direction_index][0]
                y = direction[direction_index][1]

        return board





