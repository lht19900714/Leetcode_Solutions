
// Space: O(1)
// Time: O(n)

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int maxValue = 1000000;
        if (m == 1 && n == 1) return mat;
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (mat[y][x] != 0) {
                    int left = x - 1 >= 0 ? mat[y][x - 1] : maxValue;
                    int top = y - 1 >= 0 ? mat[y - 1][x] : maxValue;
                    mat[y][x] = Math.min(left + 1, top + 1);
                }
            }
        }
        for (int y = m - 1; y >= 0; y--) {
            for (int x = n - 1; x >= 0; x--) {
                int right = x + 1 < n ? mat[y][x + 1] : maxValue;
                int bottom = y + 1 < m ? mat[y + 1][x] : maxValue;
                mat[y][x] = Math.min(mat[y][x],Math.min(right+1,bottom+1));
            }
        }
        return mat;
    }
}




