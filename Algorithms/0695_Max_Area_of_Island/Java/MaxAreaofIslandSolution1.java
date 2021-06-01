
// Space: O(n)
// Time: O(n)

class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int res = 0;
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (grid[y][x] == 1) {
                    res = Math.max(res, dfs(grid, y, x, m, n));
                }
            }
        }
        return res;
    }

    private int dfs(int[][] board, int y, int x, int m, int n) {
        if (!(0 <= y && y < m && 0 <= x && x < n)) return 0;
        if (board[y][x] == 0) return 0;
        int res = 0;
        board[y][x] = 0;
        res += 1;
        res += dfs(board, y - 1, x, m, n);
        res += dfs(board, y + 1, x, m, n);
        res += dfs(board, y, x - 1, m, n);
        res += dfs(board, y, x + 1, m, n);
        return res;
    }
}




