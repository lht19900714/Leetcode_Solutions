
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
    public int goodNodes(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return 1;
        int count = 0;
        Queue<List<Object>> queue = new ArrayDeque();
        List<Object> temp = new ArrayList<>();
        temp.add(root);
        temp.add(root.val);
        queue.add(temp);
        while (!queue.isEmpty()) {
            List cur = queue.poll();
            TreeNode curNode = (TreeNode) cur.get(0);
            Integer curNum = (Integer) cur.get(1);
            if (curNode.val >= curNum) count++;
            if (curNode.left != null) {
                List<Object> left = new ArrayList();
                left.add(curNode.left);
                left.add(Math.max(curNode.val, curNum));
                queue.add(left);
            }
            if (curNode.right != null) {
                List<Object> right = new ArrayList();
                right.add(curNode.right);
                right.add(Math.max(curNode.val, curNum));
                queue.add(right);
            }
        }
        return count;
    }
}




