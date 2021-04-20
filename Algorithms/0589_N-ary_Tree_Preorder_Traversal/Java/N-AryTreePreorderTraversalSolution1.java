
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

    public List<Integer> preorder(Node root) {
        if (root == null) return new ArrayList<>();
        if (root.children == null) return new ArrayList<Integer>(Arrays.asList(root.val));

        List<Integer> res = new ArrayList<>();
        List<Node> queue = new ArrayList<>();
        queue.add(root);

        while (queue.size() > 0) {
            Node cur = queue.remove(0);
            res.add(cur.val);
            if (cur.children != null) {
                cur.children.addAll(queue);
                queue = cur.children;
            }
        }
        return res;
    }
}




