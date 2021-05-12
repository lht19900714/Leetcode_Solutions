
// Space: O(1)
// Time: O(n)

public class NumMatrix {

    int[][] board;

    public NumMatrix(int[][] matrix) {
        board = matrix;
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int res = 0;
        for (int y = row1; y <= row2; y++) {
            for (int x = col1; x <= col2; x++) {
                res += this.board[y][x];
            }
        }
        return res;
    }
}




