
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

    public int sumOfLeftLeaves(TreeNode root) {
        dfs(root,false);
        return res;
    }

    private void dfs(TreeNode root, boolean flag) {
        if (root == null) return;
        if (root.left == null && root.right == null) {
            res += flag ? root.val : 0;
        }
        dfs(root.left, true);
        dfs(root.right, false);
    }
}




