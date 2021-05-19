
// Space: O(1)
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
        if (root.left == null & root.right == null) return;
        dfs(root);
    }

    private TreeNode dfs(TreeNode root) {
        if (root == null) return null;
        TreeNode leftLast = dfs(root.left);
        TreeNode rightLast = dfs(root.right);
        if (leftLast != null) {
            leftLast.right = root.right;
            root.right = root.left;
            root.left = null;
        }
        if (rightLast != null) return rightLast;
        if (leftLast != null) return leftLast;
        return root;
    }
}




