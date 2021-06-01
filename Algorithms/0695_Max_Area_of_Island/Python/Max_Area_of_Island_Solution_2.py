
# Space: O(n)
# Time: O(n)

class Solution:
    def maxAreaOfIsland(self, grid):
        res = 0
        m = len(grid)
        n = len(grid[0])

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    temp_res = 0
                    grid[y][x] = 0
                    stack = [[y, x]]
                    while stack:
                        cur_y, cur_x = stack.pop()
                        temp_res += 1
                        if 0 <= cur_y - 1 < m and 0 <= cur_x < n and grid[cur_y - 1][cur_x] == 1:
                            grid[cur_y - 1][cur_x] = 0
                            stack.append([cur_y - 1, cur_x])
                        if 0 <= cur_y + 1 < m and 0 <= cur_x < n and grid[cur_y + 1][cur_x] == 1:
                            grid[cur_y + 1][cur_x] = 0
                            stack.append([cur_y + 1, cur_x])
                        if 0 <= cur_y < m and 0 <= cur_x - 1 < n and grid[cur_y][cur_x - 1] == 1:
                            grid[cur_y][cur_x - 1] = 0
                            stack.append([cur_y, cur_x - 1])
                        if 0 <= cur_y < m and 0 <= cur_x + 1 < n and grid[cur_y][cur_x + 1] == 1:
                            grid[cur_y][cur_x + 1] = 0
                            stack.append([cur_y, cur_x + 1])
                    res = max(res, temp_res)
        return res





