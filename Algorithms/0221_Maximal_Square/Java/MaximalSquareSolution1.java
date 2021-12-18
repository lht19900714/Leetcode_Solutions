
// Space: O(n)
// Time: O(n)

class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix.length == 1 && matrix[0].length == 1) {
            return matrix[0][0] == '1' ? 1 : 0;
        }
        int[][] dp = new int[matrix.length][matrix[0].length];
        for (int[] row : dp) {
            Arrays.fill(row, 0);
        }
        int res = 0;
        for (int y = 0; y < matrix.length; y++) {
            for (int x = 0; x < matrix[0].length; x++) {
                if (y == 0 || x == 0) {
                    dp[y][x] = Character.getNumericValue(matrix[y][x]);
                } else if (matrix[y][x] == '1') {
                    dp[y][x] = Math.min(Math.min(dp[y - 1][x], dp[y - 1][x - 1]), dp[y][x - 1]) + 1;
                }
                res = Math.max(res, dp[y][x]);
            }
        }
        return res * res;
    }
}





