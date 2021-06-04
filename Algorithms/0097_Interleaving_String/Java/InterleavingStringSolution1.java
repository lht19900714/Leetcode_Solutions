
// Space: O(n)
// Time: O(n)

class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() == s2.length() && s2.length() == s3.length() && s3.length() == 0) return true;
        if (s1.length() + s2.length() != s3.length()) return false;
        int[][] cache = new int[s1.length()][s2.length()];
        for (int[] row : cache) {
            Arrays.fill(row, -1);
        }
        return dfs(cache, s1, s2, s3, 0, 0, 0);
    }

    private boolean dfs(int[][] board, String s1, String s2, String s3, int i1, int i2, int i3) {
        if (i1 == s1.length()) return s2.substring(i2).equals(s3.substring(i3));
        if (i2 == s2.length()) return s1.substring(i1).equals(s3.substring(i3));
        if (board[i1][i2] != -1) return board[i1][i2] == 1;

        boolean ans = false;
        if (s1.charAt(i1) == s3.charAt(i3) && dfs(board, s1, s2, s3, i1 + 1, i2, i3 + 1)) ans = true;
        if (s2.charAt(i2) == s3.charAt(i3) && dfs(board, s1, s2, s3, i1, i2 + 1, i3 + 1)) ans = true;

        board[i1][i2] = ans ? 1 : 0;
        return ans;
    }
}




