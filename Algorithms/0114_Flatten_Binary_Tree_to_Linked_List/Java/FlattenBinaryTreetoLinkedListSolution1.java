
// Space: O(n)
// Time: O(n)

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public void flatten(TreeNode root) {
        if (root == null) return;
        if (root.left == null && root.right == null) return;
        Stack<TreeNode> stack = new Stack<>();
        stack.add(root);

        while (stack.size() > 0) {
            TreeNode cur = stack.pop();
            if (cur.right != null) stack.add(cur.right);
            if (cur.left != null) stack.add(cur.left);
            if (stack.size() > 0) cur.right = stack.peek();
            cur.left = null;
        }
    }
}




