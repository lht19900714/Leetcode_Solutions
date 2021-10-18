
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
    private int xLevel = -1;
    private int yLevel = -1;
    private TreeNode xParent = null;
    private TreeNode yParent = null;
    public boolean isCousins(TreeNode root, int x, int y) {
        dfs(root, null, 0, x, y);
        return xLevel == yLevel && xParent != yParent;
    }

    private void dfs(TreeNode root, TreeNode parent, int level, int x, int y) {
        if (x == root.val) {
            xLevel = level;
            xParent = parent;
        }
        if (y == root.val) {
            yLevel = level;
            yParent = parent;
        }
        if (xLevel != -1 && yLevel != -1) return;
        if (root.left != null) dfs(root.left, root, level + 1, x, y);
        if (root.right != null) dfs(root.right, root, level + 1, x, y);
    }
}




