
# Space: O(1)
# Time: O(n)

class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        counter = m * n
        x, y = 0, 0
        res = []
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_index = 0

        while 0 <= x < n and 0 <= y < m and counter > 0:
            res.append(matrix[y][x])
            visited[y][x] = 1
            counter -= 1

            next_x = x + direction[direction_index][1]
            next_y = y + direction[direction_index][0]

            if not (0 <= next_x < n and 0 <= next_y < m) or visited[next_y][next_x] == 1:
                direction_index = (direction_index + 1) % len(direction)
                next_x = x + direction[direction_index][1]
                next_y = y + direction[direction_index][0]

            x, y = next_x, next_y

        return res




