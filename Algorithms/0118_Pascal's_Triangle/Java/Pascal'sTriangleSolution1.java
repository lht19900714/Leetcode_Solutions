
// Space: O(n)
// Time: O(n)

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        if (numRows == 1) {
            res.add(Arrays.asList(1));
            return res;
        }
        List<Integer> prevRow = null;
        for (int i = 1; i <= numRows; i++) {
            List<Integer> temp = new ArrayList<>();
            for (int j = 0; j < i; j++) {
                if (j == 0 || j == i - 1) {
                    temp.add(1);
                } else {
                    temp.add(prevRow.get(j - 1) + prevRow.get(j));
                }
            }
            prevRow = temp;
            res.add(temp);
        }
        return res;
    }
}




