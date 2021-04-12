
// Space: O(1)
// Time: O(n)

// DFS approach

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
    private int res = 0;
    private int deepestLevel = 0;

    public int deepestLeavesSum(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return root.val;
        dfs(root, 0);
        return this.res;
    }

    private void dfs(TreeNode node, int level) {
        if (node.left == null && node.right == null) {
            if (level == this.deepestLevel) {
                this.res += node.val;
            } else if (level > this.deepestLevel) {
                this.deepestLevel = level;
                this.res = node.val;
            }
            return;
        }
        if (node.left != null) dfs(node.left, level + 1);
        if (node.right != null) dfs(node.right, level + 1);
    }
}




