
// Space: O(n)
// Time: O(n)

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
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
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        if (head.next == null) return new TreeNode(head.val);
        List<Integer> cache = new ArrayList<>();
        while (head != null) {
            cache.add(head.val);
            head = head.next;
        }
        return buildTree(cache);
    }

    private TreeNode buildTree(List<Integer> ints) {
        if (ints.size() == 0) return null;
        if (ints.size() == 1) return new TreeNode(ints.get(0));
        int mid = ints.size() / 2;
        TreeNode head = new TreeNode(ints.get(mid));
        head.left = buildTree(ints.subList(0, mid));
        head.right = buildTree(ints.subList(mid + 1, ints.size()));
        return head;
    }
}




