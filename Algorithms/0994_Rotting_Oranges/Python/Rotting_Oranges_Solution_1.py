
# Space: O(n)
# Time: O(n)


class Solution:
    def orangesRotting(self, grid):
        row_number = len(grid)
        if row_number == 0: return 0
        column_number = len(grid[0])

        fresh_orange, rotten_orange = 0, 0
        queue = []
        for y in range(row_number):
            for x in range(column_number):
                if grid[y][x] == 1:
                    fresh_orange += 1
                if grid[y][x] == 2:
                    rotten_orange += 1
                    queue.append([y, x, 0])

        if fresh_orange == 0: return 0
        if rotten_orange == 0: return -1

        res = 0

        while queue:
            cur_y, cur_x, cur_time = queue.pop(0)
            res = max(res, cur_time)
            if 0 <= cur_y - 1 < row_number and 0 <= cur_x < column_number and grid[cur_y - 1][cur_x] == 1:
                grid[cur_y - 1][cur_x] = 2
                fresh_orange -= 1
                queue.append([cur_y - 1, cur_x, cur_time + 1])
            if 0 <= cur_y + 1 < row_number and 0 <= cur_x < column_number and grid[cur_y + 1][cur_x] == 1:
                grid[cur_y + 1][cur_x] = 2
                fresh_orange -= 1
                queue.append([cur_y + 1, cur_x, cur_time + 1])
            if 0 <= cur_y < row_number and 0 <= cur_x - 1 < column_number and grid[cur_y][cur_x - 1] == 1:
                grid[cur_y][cur_x - 1] = 2
                fresh_orange -= 1
                queue.append([cur_y, cur_x - 1, cur_time + 1])
            if 0 <= cur_y < row_number and 0 <= cur_x + 1 < column_number and grid[cur_y][cur_x + 1] == 1:
                grid[cur_y][cur_x + 1] = 2
                fresh_orange -= 1
                queue.append([cur_y, cur_x + 1, cur_time + 1])

        return res if fresh_orange == 0 else -1



