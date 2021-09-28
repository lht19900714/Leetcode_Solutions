
// Space: O(1)
// Time: O(n)

class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        int even = 0, odd = 1, temp = 0;
        while (even < nums.length && odd < nums.length) {
            if (nums[even] % 2 == 0) {
                even += 2;
            } else if (nums[odd] % 2 != 0) {
                odd += 2;
            } else {
                temp = nums[even];
                nums[even] = nums[odd];
                nums[odd] = temp;
                even += 2;
                odd += 2;
            }
        }
        return nums;
    }
}




