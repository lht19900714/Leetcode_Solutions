
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
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return root;
        if (root.val < key) {
            root.right = deleteNode(root.right, key);
        } else if (root.val > key) {
            root.left = deleteNode(root.left, key);
        } else {
            if (root.left == null && root.right == null) {
                return null;
            } else if (root.left == null || root.right == null) {
                return root.left == null ? root.right : root.left;
            } else {
                TreeNode predecessor = minNode(root.right);
                root.val = predecessor.val;
                root.right = deleteNode(root.right, predecessor.val);
            }
        }
        return root;
    }

    private TreeNode minNode(TreeNode root) {
        if (root == null) return root;
        while (root.left != null) {
            root = root.left;
        }
        return root;
    }
}





