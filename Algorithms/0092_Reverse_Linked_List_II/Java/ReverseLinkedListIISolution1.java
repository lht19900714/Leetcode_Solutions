
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

class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || head.next == null) return head;
        if (left == right) return head;
        ListNode firstPrev = null, first = null, second = null, secondNext = null, cur = head;
        int count = 1;
        while (cur != null && secondNext == null) {
            if (count == left - 1) firstPrev = cur;
            if (count == left) first = cur;
            if (count == right) second = cur;
            if (count == right + 1) secondNext = cur;
            cur = cur.next;
            count++;
        }
        second.next = null;

        if (firstPrev != null) firstPrev.next = reverseList1(first);
        else head = reverseList1(first);
        if (secondNext != null) {
            ListNode tempCur = head;
            while (tempCur.next != null) tempCur = tempCur.next;
            tempCur.next = secondNext;
        }
        return head;
    }

    private ListNode reverseList(ListNode root) {
        if (root == null || root.next == null) return root;
        ListNode temp = reverseList(root.next);
        root.next.next = root;
        root.next = null;
        return temp;
    }

    // private ListNode reverseList1(ListNode root) {
    //     if (root == null || root.next == null) return root;
    //     ListNode cur = root;
    //     ListNode prev = null;
    //     while (cur != null) {
    //         ListNode temp = cur.next;
    //         cur.next = prev;
    //         prev = cur;
    //         cur = temp;
    //     }
    //     return prev;
    // }
}




