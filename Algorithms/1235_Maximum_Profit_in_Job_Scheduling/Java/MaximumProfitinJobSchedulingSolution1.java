
// Space: O(n)
// Time: O(n^2)

class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int[] dp = new int[Arrays.stream(endTime).max().getAsInt() + 1];
        Arrays.fill(dp, 0);
        Map<Integer, List<Integer[]>> cache = new HashMap<>();
        for (int i = 0; i < endTime.length; i++) {
            cache.computeIfAbsent(endTime[i], k -> new ArrayList<>()).add(new Integer[]{startTime[i], profit[i]});
        }

        for (int i = 1; i < dp.length; i++) {
            if (cache.containsKey(i)) {
                for (Integer[] value : cache.get(i)) {
                    dp[i] = Math.max(dp[i], value[1] + dp[value[0]]);
                }
            }
            dp[i] = Math.max(dp[i], dp[i - 1]);
        }
        return dp[dp.length-1];
    }
}




