
// Space: O(n)
// Time: O(n)

class Solution {
    private int[] cache;

    public boolean canReach(int[] arr, int start) {
        if (arr.length == 1) return arr[0] == 0;

        cache = new int[arr.length];
        Arrays.fill(cache, 0);
        return dfs(arr, start);
    }

    private boolean dfs(int[] arr, int index) {
        if (arr[index] == 0) return true;
        if (cache[index] == 1) return false;
        cache[index] = 1;
        int left = index - arr[index];
        int right = index + arr[index];
        if (0 <= left && left < arr.length) {
            boolean leftRes = dfs(arr, left);
            if (leftRes) return leftRes;
        }
        if (0 <= right && right < arr.length) {
            boolean rightRes = dfs(arr, right);
            if (rightRes) return rightRes;
        }
        cache[index] = 0;
        return false;
    }
}




