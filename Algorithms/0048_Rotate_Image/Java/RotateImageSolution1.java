
// Space: O(1)
// Time: O(n)

class Solution {
    public void rotate(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        if (m == 1 && n == 1) return;

        for (int x = 0; x < n - 1; x++) {
            int offset = 1;
            for (int y = m - 2 - x; y >= 0; y--) {
                int temp = matrix[y][x];
                matrix[y][x] = matrix[y + offset][x + offset];
                matrix[y + offset][x + offset] = temp;
                offset++;
            }
        }

        for (int y = 0; y < m / 2; y++) {
            for (int x = 0; x < n; x++) {
                int temp = matrix[y][x];
                matrix[y][x] = matrix[m - 1 - y][x];
                matrix[m - 1 - y][x] = temp;
            }
        }
    }
}




