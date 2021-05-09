
// Space: O(n)
// Time: O(n)

class Solution {
    public int minDistance(String word1, String word2) {
        if (word1.equals(word2)) return 0;
        int[][] board = new int[word1.length() + 1][word2.length() + 1];
        for (int[] ints : board) {
            Arrays.fill(ints, 0);
        }
        for (int y = 1; y <= word1.length(); y++) {
            for (int x = 1; x <= word2.length(); x++) {
                if (word1.charAt(y - 1) == word2.charAt(x - 1)) {
                    board[y][x] = board[y - 1][x - 1] + 1;
                } else {
                    board[y][x] = Math.max(board[y][x - 1], board[y - 1][x]);
                }
            }
        }
        return word1.length() + word2.length() - 2 * board[word1.length()][word2.length()];
    }
}




