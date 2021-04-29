
// Space: O(1)
// Time: O(logn)

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int length = nums.length;
        if (length == 0) return new int[]{-1, -1};
        if (length == 1) {
            if (nums[0] == target) return new int[]{0, 0};
            return new int[]{-1, -1};
        }
        int[] res = new int[2];
        int left = 0, right = length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            }
        }
        if (left < length && nums[left] == target) {
            res[0] = left;
        } else {
            return new int[]{-1, -1};
        }
        left = 0;
        right = length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                left = mid + 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            }
        }
        res[1] = right;
        return res;
    }
}




