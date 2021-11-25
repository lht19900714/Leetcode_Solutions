
// Space: O(1)
// Time: O(n)

class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> res = new ArrayList<>();
        int i = 0, j = 0;
        int left = 0, right = 0;
        while (i < firstList.length && j < secondList.length) {
            left = Math.max(firstList[i][0], secondList[j][0]);
            right = Math.min(firstList[i][1], secondList[j][1]);
            if (left <= right) res.add(new int[]{left, right});

            if (firstList[i][1] < secondList[j][1]) {
                i++;
            } else {
                j++;
            }
        }
        return res.toArray(new int[res.size()][]);
    }
}




