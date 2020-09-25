
# Space: O(1)
# Time: O(n)


class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]: return []

        res = []
        x, y = 0, 0
        m, n = len(matrix), len(matrix[0])

        # [-1, 1]: go up
        # [1, -1]: go down
        direction = [[-1, 1], [1, -1]]
        direction_index = 0

        counter = m * n

        while 0 <= x < n and 0 <= y < m and counter > 0:
            res.append(matrix[y][x])
            counter -= 1

            next_x = x + direction[direction_index][1]
            next_y = y + direction[direction_index][0]

            # reset start point of next traversal
            if not (0 <= next_y < m and 0 <= next_x < n):
                # when goes up and reach the boundary:
                if direction_index == 0:
                    if x < n - 1:
                        x += 1
                        y = 0
                    else:
                        y += 1
                        x = n - 1

                # when go down and reach the boundary:
                elif direction_index == 1:
                    if y < m - 1:
                        x = 0
                        y += 1
                    else:
                        y = m - 1
                        x += 1

                direction_index = (direction_index + 1) % len(direction)

            else:
                x, y = next_x, next_y

        return res






