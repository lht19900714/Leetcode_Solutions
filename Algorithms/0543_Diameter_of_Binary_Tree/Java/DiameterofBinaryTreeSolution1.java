
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
    private int res = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return res;
    }

    private int dfs(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return 0;
        int left = 0, right = 0;
        if (root.left != null) left = dfs(root.left)+1;
        if (root.right != null) right = dfs(root.right)+1;
        res = Math.max(res, left + right);
        return Math.max(left, right);

    }
}




