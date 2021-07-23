
// Space: O(n)
// Time: O(n)

class Solution {
    public int partitionDisjoint(int[] nums) {
        if (nums.length == 2) return 1;
        int[] cache = new int[nums.length];
        Arrays.fill(cache, -1);
        int res = 0;
        cache[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            cache[i] = Math.max(nums[i], cache[i - 1]);
        }
        int rightMin = nums[nums.length - 1];
        for (int i = nums.length - 2; i >= 0; i--) {
            if (rightMin >= cache[i]) res = i;
            rightMin = Math.min(rightMin, nums[i]);
        }
        return res + 1;
    }
}




