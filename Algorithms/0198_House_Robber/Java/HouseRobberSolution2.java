
// Space: O(1)
// Time: O(n)

class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);
        int temp1 = nums[0], temp2 = Math.max(nums[0], nums[1]), counter = 2, cur = 0;

        while (counter < nums.length) {
            cur = Math.max(nums[counter] + temp1, temp2);
            temp1 = temp2;
            temp2 = cur;
            counter++;
        }
        return cur;
    }
}




