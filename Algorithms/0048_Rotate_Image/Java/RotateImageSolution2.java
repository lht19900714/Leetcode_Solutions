
// Space: O(1)
// Time: O(n)

class Solution {
    public void rotate(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        if (m == 1 && n == 1) return;

        int first = 0, last = n - 1;

        while (first < last) {
            int temp = last - first;
            for (int i = 0; i < temp; i++) {
                swap(matrix, first, first + i, first + i, last);
                swap(matrix, first, first + i, last, last - i);
                swap(matrix, first, first + i, last - i, first);
            }
            last--;
            first++;
        }

    }

    private void swap(int[][] matrix, int y1, int x1, int y2, int x2) {
        int temp = matrix[y1][x1];
        matrix[y1][x1] = matrix[y2][x2];
        matrix[y2][x2] = temp;
    }
}




