
// Space: O(n)
// Time: O(n)

class Solution {
    public int jump(int[] nums) {
        int length = nums.length;
        if (length <= 1) return 0;
        int[] cache = new int[length];
        Arrays.fill(cache, 0);

        for (int i = 0; i < length; i++) {
            if (nums[i] == 0) continue;
            for (int j = i + 1; j < i + 1 + nums[i]; j++) {
                if (j >= length) break;
                if (cache[j] == 0) cache[j] = cache[i] + 1;
            }
        }
        return cache[length - 1];
    }
}




