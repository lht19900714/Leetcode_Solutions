
// Space: O(n)
// Time: O(n)

class Solution {
    private Map<Integer, Set<Integer>> graph = new HashMap<>();

    public int[] findRedundantConnection(int[][] edges) {
        int[] res = null;
        for (int[] edge : edges) {
            if (dfs(edge[0], edge[1], new HashSet<>())) res = edge;

            Set<Integer> val = graph.getOrDefault(edge[0], new HashSet<>());
            val.add(edge[1]);
            graph.put(edge[0], val);

            Set<Integer> val1 = graph.getOrDefault(edge[1], new HashSet<>());
            val1.add(edge[0]);
            graph.put(edge[1], val1);
        }
        return res;
    }

    private boolean dfs(int start, int end, Set<Integer> visited) {
        if (visited.contains(start)) return false;
        if (start == end) return true;
        visited.add(start);

        for (Map.Entry<Integer, Set<Integer>> entry : graph.entrySet()) {
            for (Integer i : entry.getValue()) {
                if (dfs(i,end,visited)) return true;
            }
        }
        return false;
    }
}




