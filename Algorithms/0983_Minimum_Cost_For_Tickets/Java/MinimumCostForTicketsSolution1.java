
// Space: O(n)
// Time: O(n)

class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        if (days.length == 0) return 0;
        if (days.length == 1) return costs[0];

        int[] dp = new int[days[days.length - 1] + 1];
        Arrays.fill(dp, 0);
        int index = 0;
        for (int i = 1; i < dp.length; i++) {
            if (index < days.length && days[index] == i) {
                int dayPass = dp[i - 1] + costs[0];
                int weekPass = dp[Math.max(0, i - 7)] + costs[1];
                int monthPass = dp[Math.max(0, i - 30)] + costs[2];
                dp[i] = Math.min(dayPass, Math.min(weekPass, monthPass));
                index++;
            } else {
                dp[i] = dp[i - 1];
            }
        }
        return dp[dp.length - 1];
    }
}




