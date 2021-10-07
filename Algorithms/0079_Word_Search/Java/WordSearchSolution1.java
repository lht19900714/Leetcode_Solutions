
// Space: O(l)
// Time: O(m * n * l)

class Solution {
    public boolean exist(char[][] board, String word) {
        for (int y = 0; y < board.length; y++) {
            for (int x = 0; x < board[0].length; x++) {
                if (dfs(board, word, 0, y, x)) return true;
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int index, int y, int x) {
        if (index >= word.length()) return true;
        if (y < 0 || x < 0 || y == board.length || x == board[0].length) return false;
        if (board[y][x] != word.charAt(index)) return false;
        char temp = board[y][x];
        board[y][x] = '*';
        if (dfs(board, word, index + 1, y + 1, x)) return true;
        if (dfs(board, word, index + 1, y - 1, x)) return true;
        if (dfs(board, word, index + 1, y, x + 1)) return true;
        if (dfs(board, word, index + 1, y, x - 1)) return true;
        board[y][x] = temp;
        return false;
    }
}




