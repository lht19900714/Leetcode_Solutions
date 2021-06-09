
// Space: O(n)
// Time: O(n)

class Solution {
    public int maxResult(int[] nums, int k) {
        if (nums.length == 1) return nums[0];
        int[] dp = new int[nums.length];
        Deque<Integer> queue = new ArrayDeque<>();
        dp[0] = nums[0];
        queue.add(0);
        for (int i = 1; i < nums.length; i++) {
            dp[i] = nums[i] + dp[queue.peekFirst()];
            while (!queue.isEmpty() && dp[i] >= dp[queue.getLast()]) queue.pollLast();
            while (!queue.isEmpty() && i - queue.getFirst() >= k) queue.pollFirst();
            queue.add(i);
        }
        return dp[dp.length - 1];
    }
}





