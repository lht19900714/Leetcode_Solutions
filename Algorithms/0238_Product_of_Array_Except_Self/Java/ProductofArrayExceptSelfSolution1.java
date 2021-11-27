
// Space: O(n)
// Time: O(n)

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] temp1 = new int[nums.length];
        int[] temp2 = new int[nums.length];
        int[] res = new int[nums.length];
        Arrays.fill(temp1, 1);
        Arrays.fill(temp2, 1);

        for (int i = 1; i < nums.length; i++) {
            temp1[i] = temp1[i - 1] * nums[i - 1];
        }
        for (int i = nums.length - 2; i >= 0; i--) {
            temp2[i] = temp2[i + 1] * nums[i + 1];
        }
        for (int i = 0; i < res.length; i++) {
            res[i] = temp1[i] * temp2[i];
        }
        return res;
    }
}




