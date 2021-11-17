
// Space: O(n)
// Time: O(n)

class Solution {
    public int uniquePaths(int m, int n) {
        int[][] board = new int[m][n];
        for (int[] ints : board) {
            Arrays.fill(ints, 0);
        }
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (y == 0 || x == 0) {
                    board[y][x] = 1;
                } else {
                    board[y][x] = board[y - 1][x] + board[y][x - 1];
                }
            }
        }
        return board[m-1][n-1];
    }
}




