
// Space: O(n)
// Time: O(n)

public class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        int height = wall.size();
        if (height == 1) {
            return wall.get(0).size() == 1 ? 1 : 0;
        }

        List<List<Integer>> cache = new ArrayList<>();
        Map<Integer, Integer> count = new HashMap<>();
        int maxEdge = -1, res = -1, finalRes = 0;

        for (List<Integer> row : wall) {
            List<Integer> temp = new ArrayList<>();
            for (int i = 1; i < row.size(); i++) {
                int edge = row.subList(0, i).stream().mapToInt(Integer::intValue).sum();
                temp.add(edge);
            }
            cache.add(temp);
        }
        for (List<Integer> row : cache) {
            for (int e : row) {
                if (count.containsKey(e)) {
                    count.put(e, count.get(e) + 1);
                } else {
                    count.put(e, 1);
                }
                if (count.get(e) > maxEdge) {
                    maxEdge = count.get(e);
                    res = e;
                }
            }
        }
        if (res == -1) return height;
        for (List<Integer> row : cache) {
            if (!row.contains(res)) finalRes += 1;
        }
        return finalRes;
    }
}




