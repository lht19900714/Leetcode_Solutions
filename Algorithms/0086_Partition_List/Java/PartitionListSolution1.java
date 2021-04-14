
// Space: O(1)
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

class Solution {
    public ListNode partition(ListNode head, int x) {
       if (head == null || head.next == null) return head;
        ListNode temp1 = new ListNode(0);
        ListNode temp2 = new ListNode(0);
        ListNode pointer1 = temp1;
        ListNode pointer2 = temp2;
        ListNode cur = head;

        while (cur != null) {
            if (cur.val < x) {
                pointer1.next = cur;
                pointer1 = pointer1.next;
            } else if (cur.val >= x) {
                pointer2.next = cur;
                pointer2 = pointer2.next;
            }
            cur = cur.next;
        }
        pointer2.next = null;
        pointer1.next = temp2.next;
        return temp1.next;
    }
}




