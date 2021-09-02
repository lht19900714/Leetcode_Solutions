
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
    private int[] cache;
    public List<TreeNode> generateTrees(int n) {
    if (n == 1) {
            TreeNode res = new TreeNode(n);
            ArrayList<TreeNode> list = new ArrayList<>();
            list.add(res);
            return list;
        }
        cache = new int[n];
        for (int i = 0; i < n; i++) {
            cache[i] = i + 1;
        }
        return dfs(cache);
    }

    private List<TreeNode> dfs(int[] array) {
        if (array.length == 0) {
            List<TreeNode> res = new ArrayList<>();
            res.add(null);
            return res;
        }
        List<TreeNode> res = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            List<TreeNode> left = dfs(Arrays.copyOfRange(array, 0, i));
            List<TreeNode> right = dfs(Arrays.copyOfRange(array, i + 1, array.length));

            for (TreeNode leftNode : left) {
                for (TreeNode rightNode : right) {
                    TreeNode root = new TreeNode(array[i]);
                    root.left = leftNode;
                    root.right = rightNode;
                    res.add(root);
                }
            }
        }
        return res;
    }
}




                                                    