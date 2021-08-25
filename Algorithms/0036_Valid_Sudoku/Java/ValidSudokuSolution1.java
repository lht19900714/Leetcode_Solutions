
// Space: O(n)
// Time: O(n)

class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[][] startPoint = new int[][]{{0, 0}, {0, 3}, {0, 6}, {3, 0}, {3, 3}, {3, 6}, {6, 0}, {6, 3}, {6, 6}};
        if (!checkLine(board, 1)) return false;
        if (!checkLine(board, 0)) return false;
        for (int[] temp : startPoint) {
            if (!checkBox(board, temp[0], temp[1])) return false;
        }
        return true;
    }

    private boolean checkLine(char[][] board, int flag) {
        if (flag == 1) {  // check row
            for (int y = 0; y < 9; y++) {
                Set<Character> cache = new HashSet<>();
                for (int x = 0; x < 9; x++) {
                    if (board[y][x] == '.') continue;
                    if (!cache.contains(board[y][x])) {
                        cache.add(board[y][x]);
                    } else return false;
                }
            }
        } else { // check column
            for (int x = 0; x < 9; x++) {
                Set<Character> cache = new HashSet<>();
                for (int y = 0; y < 9; y++) {
                    if (board[y][x] == '.') continue;
                    if (!cache.contains(board[y][x])) {
                        cache.add(board[y][x]);
                    } else return false;
                }
            }
        }
        return true;
    }

    private boolean checkBox(char[][] board, int yStrat, int xStart) {
        Set<Character> cache = new HashSet<>();
        for (int y = yStrat; y < yStrat + 3; y++) {
            for (int x = xStart; x < xStart + 3; x++) {
                if (board[y][x] == '.') continue;
                if (!cache.contains(board[y][x])) {
                    cache.add(board[y][x]);
                } else return false;
            }
        }
        return true;
    }
}





