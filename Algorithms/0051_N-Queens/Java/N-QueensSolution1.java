
// Space: O(n)
// Time: O(n)

class Solution {
    List<List<String>> res = new ArrayList<>();
    int length = 0;

    public List<List<String>> solveNQueens(int n) {
        if (n == 1) {
            List<List<String>> res = new ArrayList<>();
            res.add(new ArrayList<>(Arrays.asList("Q")));
            return res;
        }
        length = n;
        String[][] board = new String[n][n];
        for (int row = 0; row < board.length; row++) {
            Arrays.fill(board[row], ".");
        }
        dfs(board, n, 0);
        return res;
    }

    private List<String> generateRes(String[][] board) {
        List<String> res = new ArrayList<>();
        for (int y = 0; y < board.length; y++) {
            res.add(Arrays.stream(board[y]).map(Objects::toString).collect(Collectors.joining()));
        }
        return res;
    }

    private void dfs(String[][] board, int queens, int y) {
        if (queens == 0) {
            List<String> tempRes = generateRes(board);
            res.add(tempRes);
            return;
        }
        for (int i = 0; i < length; i++) {
            if (verify(board, y, i)) {
                queens--;
                board[y][i] = "Q";
                dfs(board, queens, y + 1);
                board[y][i] = ".";
                queens++;
            }
        }
    }

    private boolean verify(String[][] board, int y, int x) {
        int tempY = 0, tempX = 0;
        // check top
        tempY = y;
        while (tempY >= 0) {
            if (board[tempY][x] == "Q") return false;
            tempY--;
        }
        // check diagonal
        tempX = x;
        tempY = y;
        while (tempY >= 0 && tempX >= 0) {
            if (board[tempY][tempX] == "Q") return false;
            tempY--;
            tempX--;
        }

        tempX = x;
        tempY = y;
        while (tempY >= 0 && tempX < length) {
            if (board[tempY][tempX] == "Q") return false;
            tempY--;
            tempX++;
        }
        return true;
    }
}




