
// Space: O(n)
// Time: O(n)

// BFS approach

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
    public int deepestLeavesSum(TreeNode root) {
        if (root.left == null && root.right == null) {
            return root.val;
        }
        int res = 0, deepestLevel = 0;
        Queue<MyData> queue = new ArrayDeque<>();
        queue.add(new MyData(root, deepestLevel));

        while (queue.size() > 0) {
            MyData cur = queue.remove();
            if (cur.node.left == null && cur.node.right == null) {
                if (cur.level > deepestLevel) {
                    res = cur.node.val;
                    deepestLevel = cur.level;
                } else if (cur.level == deepestLevel) {
                    res += cur.node.val;
                }
            }
            if (cur.node.left != null) queue.add(new MyData(cur.node.left, cur.level + 1));
            if (cur.node.right != null) queue.add(new MyData(cur.node.right, cur.level + 1));
        }
        return res;

    }

    class MyData {
        public TreeNode node;
        public int level;

        public MyData(TreeNode node, int level) {
            this.node = node;
            this.level = level;
        }
    }
}




