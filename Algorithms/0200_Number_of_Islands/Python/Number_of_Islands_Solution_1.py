
# Space: O(1)
# Time: O(n)


class Solution:
    def numIslands(self, grid):

        def dfs(grid, x, y, column, row):
            if (not 0 <= y < row) and (not 0 <= x < column): return
            if grid[y][x] != "1": return

            grid[y][x] = "0"

            dfs(grid, x - 1, y, column, row)
            dfs(grid, x + 1, y, column, row)
            dfs(grid, x, y - 1, column, row)
            dfs(grid, x, y + 1, column, row)

        row_number = len(grid)
        if row_number == 0: return 0
        column_number = len(grid[0])

        res = 0
        for y in range(row_number):
            for x in range(column_number):
                if grid[y][x] == "1":
                    dfs(grid, x, y, column_number, row_number)
                    res += 1
        return res
