
// Space: O(1)
// Time: O(n)

class Solution {
    public int minCostClimbingStairs(int[] cost) {
        if (cost.length <= 2) return Arrays.stream(cost).min().getAsInt();
        int temp1 = 0, temp2 = 0, temp3 = 0;
        for (int i = 2; i <= cost.length; i++) {
            temp3 = Math.min(temp1 + cost[i - 2], temp2 + cost[i - 1]);
            temp1 = temp2;
            temp2 = temp3;
        }
        return temp3;
    }
}




