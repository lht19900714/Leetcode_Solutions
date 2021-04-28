
// Space: O(n)
// Time: O(n)

public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid[0][0] == 1) return 0;
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[][] tempBoard = new int[m][n];
        for (int i = 0; i < tempBoard.length; i++) {
            Arrays.fill(tempBoard[i], 0);
        }
        tempBoard[0][0] = 1;
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (obstacleGrid[y][x] != 1) {
                    tempBoard[y][x] += y - 1 >= 0 ? tempBoard[y - 1][x] : 0;
                    tempBoard[y][x] += x - 1 >= 0 ? tempBoard[y][x - 1] : 0;
                }
            }
        }
        return tempBoard[m - 1][n - 1];
    }
}




