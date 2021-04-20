
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

    public List<Integer> postorder(Node root) {
        if (root == null) return new ArrayList<>();
        if (root.children == null) return new ArrayList<Integer>(Arrays.asList(root.val));

        Stack<Node> stack = new Stack<>();
        List<Integer> res = new ArrayList<>();
        stack.add(root);

        while (stack.size() > 0) {
            Node cur = stack.pop();
            res.add(cur.val);
            if (cur.children != null){
                for (Node c : cur.children) {
                    stack.add(c);
                }
            }
        }
        Collections.reverse(res);
        return res;
    }
}




