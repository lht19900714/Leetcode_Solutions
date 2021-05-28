
// Space: O(n)
// Time: O(n)

class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        if (nums.length == 1) return nums[0];
        int slow = 0, fast = 0, runningTotal = 0, res = 0;
        Set<Integer> cache = new HashSet<>();
        while (fast < nums.length) {
            if (cache.contains(nums[fast])) {
                res = Math.max(res, runningTotal);
                cache.remove(nums[slow]);
                runningTotal -= nums[slow];
                slow += 1;
            } else if (!cache.contains(nums[fast])) {
                cache.add(nums[fast]);
                runningTotal += nums[fast];
                fast += 1;
            }
        }
        res = Math.max(res, runningTotal);
        return res;
    }
}





