
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
    private int count = 0;
    public int goodNodes(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return 1;
        dfs(root,root.val);
        return count;
    }

    private void dfs(TreeNode root, int point) {
        if (root == null) return;
        if (root.val >= point) count++;
        if (root.left != null) dfs(root.left, Math.max(root.val, point));
        if (root.right != null) dfs(root.right, Math.max(root.val, point));
    }
}




