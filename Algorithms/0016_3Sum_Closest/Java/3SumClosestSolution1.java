
// Space: O(1)
// Time: O(n^2)

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if (nums.length == 3) return Arrays.stream(nums).sum();
        Arrays.sort(nums);
        int res = nums[0] + nums[1] + nums[2];
        for (int i = 1; i < nums.length - 1; i++) {
            int left = 0, right = nums.length - 1;
            while (left != i && right != i) {
                if (Math.abs(nums[left] + nums[i] + nums[right] - target) < Math.abs(res - target)) {
                    res = nums[left] + nums[i] + nums[right];
                }
                if (nums[left] + nums[i] + nums[right] == target) return res;
                if (nums[left] + nums[i] + nums[right] < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return res;
    }
}




