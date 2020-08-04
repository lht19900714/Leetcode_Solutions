# Space: O(1)
# Time: O(n)

# BFS approach

class Solution:
    def numIslands(self, grid):
        row_number = len(grid)
        if row_number == 0: return 0
        column_number = len(grid[0])

        res = 0

        for y in range(row_number):
            for x in range(column_number):
                if grid[y][x] == "1":
                    grid[y][x] = "0"
                    queue = [(y, x)]
                    while queue:
                        cur_y, cur_x = queue.pop(0)
                        if 0 <= cur_y - 1 < row_number and 0 <= cur_x < column_number and grid[cur_y - 1][cur_x] == "1":
                            grid[cur_y - 1][cur_x] = "0"
                            queue.append((cur_y - 1, cur_x))
                        if 0 <= cur_y + 1 < row_number and 0 <= cur_x < column_number and grid[cur_y + 1][cur_x] == "1":
                            grid[cur_y + 1][cur_x] = "0"
                            queue.append((cur_y + 1, cur_x))
                        if 0 <= cur_y < row_number and 0 <= cur_x - 1 < column_number and grid[cur_y][cur_x - 1] == "1":
                            grid[cur_y][cur_x - 1] = "0"
                            queue.append((cur_y, cur_x - 1))
                        if 0 <= cur_y  < row_number and 0 <= cur_x + 1 < column_number and grid[cur_y][cur_x + 1] == "1":
                            grid[cur_y][cur_x + 1] = "0"
                            queue.append((cur_y, cur_x + 1))
                    res += 1
        return res



