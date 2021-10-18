
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
    public boolean isCousins(TreeNode root, int x, int y) {
        Queue<List<TreeNode>> queue = new ArrayDeque<>();
        List<TreeNode> temp = new ArrayList<>();
        temp.add(root);
        temp.add(null);
        queue.add(temp);
        TreeNode xParent = null, yParent = null;
        int xLevel = -1, yLevel = -1;
        int level = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                List<TreeNode> cur = queue.poll();
                TreeNode curNode = cur.get(0);
                TreeNode curParentNode = cur.get(1);
                if (curNode.val == x) {
                    xParent = curParentNode;
                    xLevel = level;
                }
                if (curNode.val == y) {
                    yParent = curParentNode;
                    yLevel = level;
                }
                if (xLevel != -1 && yLevel != -1) {
                    return xParent != yParent && xLevel == yLevel;
                }
                if (curNode.left != null) {
                    ArrayList<TreeNode> left = new ArrayList<>();
                    left.add(curNode.left);
                    left.add(curNode);
                    queue.add(left);
                }
                if (curNode.right != null) {
                    ArrayList<TreeNode> right = new ArrayList<>();
                    right.add(curNode.right);
                    right.add(curNode);
                    queue.add(right);
                }
            }
            level++;
        }
        return false;
    }
}




