
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
    public TreeNode pruneTree(TreeNode root) {
        if (root == null) return root;
        if (root.left == null && root.right == null) {
            return root.val == 1 ? root : null;
        }
        int res = dfs(root);
        return res == 0 ? null : root;
    }

    private int dfs(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return root.val;

        int left = dfs(root.left);
        int right = dfs(root.right);
        if (left == 0) root.left = null;
        if (right == 0) root.right = null;

        if (left == 0 && right == 0 && root.val == 0) return 0;
        return 1;
    }
}




