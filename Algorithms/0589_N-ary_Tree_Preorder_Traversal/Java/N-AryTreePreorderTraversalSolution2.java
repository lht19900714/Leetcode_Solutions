
// Space: O(1)
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

    public List<Integer> preorder(Node root) {
        if (root == null) return new ArrayList<>();
        if (root.children == null) return new ArrayList<Integer>(Arrays.asList(root.val));
        return dfs(root);
    }

    private List<Integer> dfs(Node root) {
        if (root == null) return new ArrayList<>();
        if (root.children == null) return new ArrayList<Integer>(Arrays.asList(root.val));
        List<Integer> res = new ArrayList<>();
        res.add(root.val);
        for (Node c : root.children) {
            res.addAll(dfs(c));
        }
        return res;
    }
}




