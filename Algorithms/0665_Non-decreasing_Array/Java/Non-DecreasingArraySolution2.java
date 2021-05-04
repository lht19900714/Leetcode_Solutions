
// Space: O(n)
// Time: O(n)

class Solution {
    public boolean checkPossibility(int[] nums) {
        int length = nums.length;
        if (length <= 1) return true;
        int slow = -1, fast = 0;
        while (fast < length - 1) {
            if (!(nums[fast] <= nums[fast + 1])) {
                if (slow != -1) return false;
                slow = fast;
            }
            fast++;
        }
        if (slow == -1 || slow == 0 || slow == length - 2) return true;
        if (nums[slow - 1] <= nums[slow + 1]) return true;
        if (nums[slow] <= nums[slow + 2]) return true;
        return false;
    }
}




