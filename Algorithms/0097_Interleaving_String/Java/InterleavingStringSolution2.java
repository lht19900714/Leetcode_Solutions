
// Space: O(n)
// Time: O(n)

class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() == s2.length() && s2.length() == s3.length() && s3.length() == 0) return true;
        if (s1.length() + s2.length() != s3.length()) return false;
        s1 = "#" + s1;
        s2 = "#" + s2;
        s3 = "#" + s3;
        boolean[][] dp = new boolean[s1.length()][s2.length()];
        for (boolean[] row : dp) {
            Arrays.fill(row, false);
        }

        for (int y = 0; y < s1.length(); y++) {
            for (int x = 0; x < s2.length(); x++) {
                if (x == 0 && y == 0) dp[y][x] = true;
                else if (y == 0 && s2.charAt(x) == s3.charAt(x + y) && dp[y][x - 1]) dp[y][x] = true;
                else if (x == 0 && s1.charAt(y) == s3.charAt(x + y) && dp[y - 1][x]) dp[y][x] = true;
                else if (s2.charAt(x) == s3.charAt(x + y) && dp[y][x - 1]) dp[y][x] = true;
                else if (s1.charAt(y) == s3.charAt(x + y) && dp[y - 1][x]) dp[y][x] = true;
            }
        }
        return dp[s1.length() - 1][s2.length() - 1];
    }
}





