
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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder.length == 0) return null;
        if (inorder.length == 1) return new TreeNode(inorder[0]);
        postorderIndex = postorder.length - 1;
        return constructTree(inorder,postorder);
    }

    private int postorderIndex;

    private TreeNode constructTree(int[] inorder, int[] postorder) {
        if (postorderIndex < 0 || inorder.length == 0 || postorder.length == 0) return null;
        int rootVal = postorder[postorderIndex--];
        TreeNode root = new TreeNode(rootVal);
        int inorderIndex = findIndex(inorder, rootVal);
        if (inorderIndex != -1){
            root.right = constructTree(Arrays.copyOfRange(inorder, inorderIndex + 1, inorder.length), postorder);
            root.left = constructTree(Arrays.copyOfRange(inorder, 0, inorderIndex), postorder);
        }
        return root;
    }

    private int findIndex(int[] array, int target) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == target) return i;
        }
        return -1;
    }
}




