
// Space: O(n)
// Time: O(n)

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    private Map<Integer, List<Integer>> cache;
    private List<List<Integer>> res;

    public List<List<Integer>> levelOrder(Node root) {
        if (root == null) return new ArrayList<>();
        cache = new HashMap<>();
        res = new ArrayList<>();
        Queue<Node> queue = new ArrayDeque<>();
        queue.add(root);
        int level = 0;
        while (!queue.isEmpty()) {
            int length = queue.size();
            while (length-- > 0) {
                Node curRoot = queue.poll();
                cache.computeIfAbsent(level, k -> new ArrayList<>()).add(curRoot.val);
                if (curRoot.children != null) {
                    for (Node child : curRoot.children) {
                        queue.add(child);
                    }
                }
            }
            level++;
        }
        for (int i = 0; i < cache.size(); i++) {
            res.add(cache.get(i));
        }
        return res;
    }
}




