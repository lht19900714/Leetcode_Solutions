
// Space: O(n)
// Time: O(n)

class Solution {
    private Map<String, Boolean> cache;

    public boolean stoneGame(int[] piles) {
        if (piles.length <= 2) return true;
        cache = new HashMap<>();
        return dfs(0, piles.length - 1, piles, 0, 0, 1);
    }

    private boolean dfs(int left, int right, int[] piles, int alex, int lee, int flag) {
        if (left > right) return alex > lee;
        String key = left + "," + right;
        if (cache.containsKey(key)) return cache.get(key);
        boolean res = false;

        // flag==1: alex turn
        // flag==0: lee turn
        if (flag == 1) {
            alex += piles[left];
            res = dfs(left + 1, right, piles, alex, lee, 0);
            alex -= piles[left];
            cache.put(key, res);
            if (res) return res;

            alex += piles[right];
            res = dfs(left, right - 1, piles, alex, lee, 0);
            alex -= piles[right];
            cache.put(key, res);
            if (res) return res;
        }
        if (flag == 0) {
            lee += piles[left];
            res = dfs(left + 1, right, piles, alex, lee, 1);
            lee -= piles[left];
            cache.put(key, res);
            if (res) return res;

            lee += piles[right];
            res = dfs(left, right - 1, piles, alex, lee, 1);
            lee -= piles[right];
            cache.put(key, res);
            if (res) return res;
        }
        return res;
    }
}




