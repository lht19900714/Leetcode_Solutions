
// Space: O(n)
// Time: O(n)

class Solution {

    private HashMap<String, Integer> cache = new HashMap<>();

    public int minimumTotal(List<List<Integer>> triangle) {
        int height = triangle.size();
        if (height == 1) return triangle.get(0).get(0);

        for (int x = 0; x < triangle.get(height - 1).size(); x++) {
            String key = x + "_" + Integer.toString(height - 1);
            cache.put(key, triangle.get(height - 1).get(x));
        }

        return dfs(triangle, 0, 0);
    }

    private int dfs(List<List<Integer>> triangle, int x, int y) {
        if (cache.containsKey(x + "_" + y)) return cache.get(x + "_" + y);
        int res = triangle.get(y).get(x) + Math.min(dfs(triangle, x, y + 1), dfs(triangle, x + 1, y + 1));
        cache.put(x + "_" + y, res);
        return res;
    }
}









