
// Space: O(n)
// Time: O(n)

class Solution {

    public int minimumTotal(List<List<Integer>> triangle) {
        int height = triangle.size();
        if (height == 1) return triangle.get(0).get(0);
        int[] cache = new int[height];

        for (int i = 0; i < triangle.get(height - 1).size(); i++) {
            cache[i] = triangle.get(height - 1).get(i);
        }
        for (int y = height - 2; y >= 0; y--) {
            for (int x = 0; x < triangle.get(y).size(); x++) {
                cache[x] = triangle.get(y).get(x) + Math.min(cache[x], cache[x + 1]);
            }
        }
        return cache[0];
    }
}






