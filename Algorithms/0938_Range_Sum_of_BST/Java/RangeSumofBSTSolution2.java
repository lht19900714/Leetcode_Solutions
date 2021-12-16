
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
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) return 0;
        if (root.left == null && root.right == null && low <= root.val && root.val <= high) return root.val;
        return dfs(root,low,high);
    }

    private int dfs(TreeNode root, int low, int high) {
        if (root == null) return 0;
        if (root.val<low) return dfs(root.right,low,high);
        if (root.val>high) return dfs(root.left,low,high);
        return dfs(root.left,low,high) + root.val + dfs(root.right,low,high);
    }
}




