// Space: O(1)
// Time: O(logn)

class Solution {
    public int singleNonDuplicate(int[] nums) {
        if (nums.length == 1) return nums[0];
        int left = 0, right = nums.length - 1;
        int mid, midPair;
        while (left < right) {
            mid = left + (right - left) / 2;
            midPair = mid % 2 == 0 ? mid + 1 : mid - 1;
            if (nums[mid] == nums[midPair]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left];
    }
}




