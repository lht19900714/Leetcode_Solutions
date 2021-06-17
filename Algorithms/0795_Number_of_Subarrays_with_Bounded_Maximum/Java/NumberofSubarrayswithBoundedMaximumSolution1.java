
// Space: O(1)
// Time: O(n)

class Solution {
    public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        if (nums.length == 1) {
            return nums[0] >= left && nums[0] <= right ? 1 : 0;
        }
        int slow = 0, fast = 0, count = 0, res = 0;
        while (fast < nums.length) {
            if (left <= nums[fast] & nums[fast] <= right) {
                count = fast - slow + 1;
                res += count;
            } else if (nums[fast] < left) {
                res += count;
            } else if (right < nums[fast]) {
                slow = fast+1;
                count = 0;
            }
            fast++;
        }
        return res;
    }
}




