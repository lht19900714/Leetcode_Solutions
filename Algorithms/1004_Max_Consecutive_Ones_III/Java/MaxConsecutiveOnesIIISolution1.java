
// Space: O(1)
// Time: O(n)

class Solution {
    public int longestOnes(int[] nums, int k) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return k > 0 ? 1 : 0;
        int slow = 0, fast = 0, res = 0, count = k;
        while (fast < nums.length) {
            if (nums[fast] == 0 && count > 0) {
                count--;
                fast++;
            } else if (nums[fast] == 1) {
                fast++;
            } else if (count == 0) {
                res = Math.max(fast - slow, res);
                if (nums[slow] == 0) count++;
                slow++;
            }
        }
        res = Math.max(fast - slow, res);
        return res;
    }
}




