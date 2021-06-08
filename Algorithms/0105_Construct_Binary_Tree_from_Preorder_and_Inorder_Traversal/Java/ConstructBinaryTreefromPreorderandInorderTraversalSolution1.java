
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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 1) return new TreeNode(preorder[0]);
        List<Integer> preList = new ArrayList<>(), inList = new ArrayList<>();
        for (int p : preorder) preList.add(p);
        for (int i : inorder) inList.add(i);
        return dfs(preList, inList);
    }

    private TreeNode dfs(List<Integer> pre, List<Integer> in) {
        if (pre.size() == 0 || in.size() == 0) return null;
        int val = pre.remove(0);
        int index = in.indexOf(val);
        TreeNode root = new TreeNode(val);
        List<Integer> left = in.subList(0, index);
        List<Integer> right = in.subList(index + 1, in.size());
        root.left = dfs(pre, left);
        root.right = dfs(pre, right);
        return root;
    }
}




