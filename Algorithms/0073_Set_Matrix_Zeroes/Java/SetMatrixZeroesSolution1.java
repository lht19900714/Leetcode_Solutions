
// Space: O(n)
// Time: O(n)

class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix.length == 0) return;
        Set<Integer> row = new HashSet<>();
        Set<Integer> column = new HashSet<>();

        for (int y = 0; y < matrix.length; y++) {
            for (int x = 0; x < matrix[0].length; x++) {
                if (matrix[y][x] == 0) {
                    row.add(y);
                    column.add(x);
                }
            }
        }
        for (Integer i : row) {
            Arrays.fill(matrix[i], 0);
        }
        for (Integer i : column) {
            int temp = 0;
            while (temp < matrix.length) {
                matrix[temp][i] = 0;
                temp++;
            }
        }
    }
}




