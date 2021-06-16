
// Space: O(n)
// Time: O(n^2)

class Solution {
    private int[] cache = new int[4];

    public boolean makesquare(int[] matchsticks) {
        if (matchsticks.length == 0) return false;
        int sum = Arrays.stream(matchsticks).sum();
        int length = sum / 4;
        if (length * 4 != sum) return false;
        Arrays.fill(cache, 0);

        Arrays.sort(matchsticks);
        for (int i = 0, j = matchsticks.length - 1; i < j; i++, j--) {
            int temp = matchsticks[i];
            matchsticks[i] = matchsticks[j];
            matchsticks[j] = temp;
        }
        return dfs(matchsticks, length, 0);
    }

    private boolean dfs(int[] alist, int target, int index) {
        if (index == alist.length) {
            return cache[0] == cache[1] && cache[1] == cache[2] && cache[2] == target;
        }
        for (int i = 0; i < 4; i++) {
            if (cache[i] + alist[index] <= target) {
                cache[i] += alist[index];
                if (dfs(alist, target, index + 1)) return true;
                cache[i] -= alist[index];
            }
        }
        return false;
    }
}




