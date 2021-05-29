

// Space: O(n)
// Time: O(n)

class Solution {
    int res = 0;

    public int totalNQueens(int n) {
        if (n <= 1) return n;
        String[][] board = new String[n][n];
        for (String[] row : board) {
            Arrays.fill(row, ".");
        }
        dfs(board, n, 0);
        return res;
    }

    private void dfs(String[][] board, int queens, int row) {
        if (queens == 0) {
            res += 1;
            return;
        }
        for (int i = 0; i < board.length; i++) {
            if (verify(board, row, i)) {
                board[row][i] = "Q";
                dfs(board, queens - 1, row + 1);
                board[row][i] = ".";
            }
        }
    }

    private boolean verify(String[][] board, int y, int x) {
        int temp_y = y;
        int temp_x = x;
        while (temp_y >= 0) {
            if (board[temp_y][x] != ".") return false;
            temp_y -= 1;
        }
        temp_y = y;
        while (temp_y >= 0 && temp_x >= 0) {
            if (board[temp_y][temp_x] != ".") return false;
            temp_y -= 1;
            temp_x -= 1;
        }
        temp_y = y;
        temp_x = x;
        while (temp_y >= 0 && temp_x < board.length) {
            if (board[temp_y][temp_x] != ".") return false;
            temp_y -= 1;
            temp_x += 1;
        }
        return true;
    }
}




