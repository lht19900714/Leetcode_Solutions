
// Space: O(n)
// Time: O(n)

class Solution {
    public boolean judgeSquareSum(int c) {
        if (c <= 2) return true;
        int temp = (int) Math.pow(c, 0.5) + 1;
        int[] cache = new int[temp];
        for (int i = 0; i < cache.length; i++) {
            cache[i] = i;
        }
        int left = 0, right = cache.length - 1;
        while (left <= right) {
            if (left * left + right * right == c) return true;
            if (left * left + right * right > c) {
                right--;
            } else if (left * left + right * right < c) {
                left++;
            }
        }
        return false;
    }
}




