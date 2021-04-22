
// Space: O(n)
// Time: O(n)

public class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        int height = wall.size();
        if (height == 1) {
            return wall.get(0).size() == 1 ? 1 : 0;
        }

        Map<Integer, Integer> cache = new HashMap<>();
        int maxEdge = 0;

        for (List<Integer> row : wall) {
            for (int i = 1; i < row.size(); i++) {
                int edge = row.subList(0, i).stream().reduce(Integer::sum).get();
                if (cache.containsKey(edge)) {
                    cache.put(edge, cache.get(edge) + 1);
                } else {
                    cache.put(edge, 1);
                }
                maxEdge = cache.get(edge) > maxEdge ? cache.get(edge) : maxEdge;
            }
        }
        return height - maxEdge;
    }
}




