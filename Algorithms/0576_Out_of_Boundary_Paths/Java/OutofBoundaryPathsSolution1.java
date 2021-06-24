
// Space: O(n)
// Time: O(n)

class Solution {
    private int mod = 1000000007;
    private int[][][] board = null;

    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        board = new int[maxMove + 1][m][n];
        for (int[][] temp : board) {
            for (int[] row : temp) {
                Arrays.fill(row, -1);
            }
        }
        return (int)dfs(m, n, startRow, startColumn, maxMove);

    }
    private int dfs(int row, int column, int y, int x, int n) {
        if (!(0 <= y && y < row) || !(0 <= x && x < column)) return 1;
        if (n <= 0) return 0;
        if (board[n][y][x] != -1) return board[n][y][x];

        int tempRes = 0;
        tempRes = tempRes % mod + dfs(row, column, y - 1, x, n - 1) % mod;
        tempRes = tempRes % mod + dfs(row, column, y + 1, x, n - 1) % mod;
        tempRes = tempRes % mod + dfs(row, column, y, x - 1, n - 1) % mod;
        tempRes = tempRes % mod + dfs(row, column, y, x + 1, n - 1) % mod;

        board[n][y][x] = tempRes % mod;
        return board[n][y][x];
    }
}





