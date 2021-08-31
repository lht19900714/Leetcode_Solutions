
// Space: O(1)
// Time: O(n)

class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        if (ops.length == 0) return m * n;
        int row = ops[0][0], column = ops[0][1];

        for (int[] item : ops) {
            row = Math.min(row, item[0]);
            column = Math.min(column, item[1]);
        }
        return row * column;
    }
}




