
// Space: O(n)
// Time: O(n)

class Solution {
    private List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<Integer> temp = new ArrayList<>();
        temp.add(0);
        dfs(graph, graph[0], temp, graph.length - 1);
        return res;
    }

    private void dfs(int[][] graph, int[] nodeList, List<Integer> temp, int endNode) {
        if (temp.get(temp.size() - 1) == endNode) {
            res.add(new ArrayList<>(temp));
            return;
        }
        for (int node : nodeList) {
            temp.add(node);
            dfs(graph, graph[node], temp, endNode);
            temp.remove(temp.size() - 1);
        }
    }
}

                


