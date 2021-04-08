
# Space: O(n)
# Time: O(n)


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1: return -1
        m = len(grid)
        n = len(grid[0])
        res = -1
        visited = set()
        queue = [[0, 0, 1]]  # [x,y,step]
        direction = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]  # [x_direction,y_direction]

        while queue:
            x, y, step = queue.pop(0)
            if (x, y) in visited: continue
            if x == n - 1 and y == m - 1:
                res = min(res, step) if res != -1 else step

            for dir_x, dir_y in direction:
                new_x, new_y = x + dir_x, y + dir_y
                if 0 <= new_x < n and 0 <= new_y < m and grid[new_y][new_x] == 0:
                    queue.append([new_x, new_y, step + 1])

            visited.add((x, y))

        return res





