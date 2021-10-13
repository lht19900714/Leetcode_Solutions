
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
    public TreeNode bstFromPreorder(int[] preorder) {
        if (preorder.length == 0) return null;
        if (preorder.length == 1) return new TreeNode(preorder[0]);
        TreeNode root = new TreeNode(preorder[0]);
        int index = 1;
        int [] left , right;
        while (index < preorder.length && preorder[index]<preorder[0]) {
                index++;
        }
        left = Arrays.copyOfRange(preorder,1,index);
        right = Arrays.copyOfRange(preorder,index,preorder.length);
        root.left = bstFromPreorder(left);
        root.right = bstFromPreorder(right);
        return root;
    }
}




