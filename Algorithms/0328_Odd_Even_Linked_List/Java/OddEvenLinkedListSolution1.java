
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
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) return head;
        ListNode oddHead = new ListNode(0), evenHead = new ListNode(0);
        ListNode oddCur = oddHead, evenCur = evenHead;
        ListNode cur = head;
        int counter = 1;
        while (cur != null) {
            if (counter % 2 == 1) {
                oddCur.next = cur;
                oddCur = oddCur.next;
            } else if (counter % 2 == 0) {
                evenCur.next = cur;
                evenCur = evenCur.next;
            }
            cur = cur.next;
            counter++;
        }
        oddCur.next = evenHead.next;
        evenCur.next = null;
        return oddHead.next;
    }
}




