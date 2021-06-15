
// Space: O(1)
// Time: O(n)

class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        if (boxTypes.length == 1) {
            return boxTypes[0][0] <= truckSize ? boxTypes[0][1] : 0;
        }
        int res = 0;

        Arrays.sort(boxTypes, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o2[1] != o1[1]) {
                    return o2[1] - o1[1];
                } else {
                    return o1[0] - o2[0];
                }
            }
        });
        for (int[] boxType : boxTypes) {
            if (truckSize == 0) return res;
            int tempCount = Math.min(truckSize, boxType[0]);
            res += tempCount * boxType[1];
            truckSize -= tempCount;
        }
        return res;
    }
}




