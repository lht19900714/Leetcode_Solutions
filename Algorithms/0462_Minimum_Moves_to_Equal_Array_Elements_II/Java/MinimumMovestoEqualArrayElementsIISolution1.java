
// Space: O(1)
// Time: O(n)

class Solution {
    public int minMoves2(int[] nums) {
        if (nums.length <= 1) return 0;
        Arrays.sort(nums);
        int res = 0;
        int mid = nums.length / 2;
        for (int i = 0; i < nums.length; i++) {
            res += Math.abs(nums[i] - nums[mid]);
        }
        return res;
    }
}




