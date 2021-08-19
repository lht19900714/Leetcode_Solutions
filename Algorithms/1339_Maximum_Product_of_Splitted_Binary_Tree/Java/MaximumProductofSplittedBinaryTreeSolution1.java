
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
    private Map<TreeNode, Long> cache = new HashMap<>();

    public int maxProduct(TreeNode root) {
        dfs(root);
        int mod = 1000000007;
        long totalSum = cache.get(root), res = 0;
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode cur = queue.poll();
            if (cur.left != null) {
                res = Math.max(res, (totalSum - cache.get(cur.left)) * cache.get(cur.left));
                queue.add(cur.left);
            }
            if (cur.right != null) {
                res = Math.max(res, (totalSum - cache.get(cur.right)) * cache.get(cur.right));
                queue.add(cur.right);
            }
        }
        return (int) (res % mod);
    }

    private long dfs(TreeNode root) {
        if (root == null) return 0;
        if (cache.containsKey(root)) return cache.get(root);
        cache.put(root, dfs(root.left) + dfs(root.right) + root.val);
        return cache.get(root);
    }
}
         



