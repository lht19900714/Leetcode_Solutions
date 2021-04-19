
// Space: O(n)
// Time: O(n)

public class Solution {

    public int combinationSum4(int[] nums, int target) {
        Arrays.sort(nums);
        if (nums[0] > target) return 0;

        int[] dp = new int[target + 1];
        for (int num : nums) {
            if (num < dp.length) dp[num] = 1;
        }

        for (int i = 1; i < dp.length; i++) {
            for (int num : nums) {
                if (i + num <= target) dp[i + num] += dp[i];
            }
        }
        return dp[dp.length - 1];
    }
}







