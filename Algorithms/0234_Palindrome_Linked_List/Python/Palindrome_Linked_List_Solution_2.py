
# Space: O(1)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head):
        if not head: return True
        if head.next is None: return True

        def reverse_linked_list(head):
            if not head: return head
            if head.next is None: return head

            cur, prev = head, None
            while cur:
                cur.next, cur, prev = prev, cur.next, cur

            return prev

        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # If fast pointer stop at last node, it means the length of linked list is odd number, then we should move slow pointer to next one.
        # If fast pointer is None, it means the length of linked list is even number, then no need to move slow pointer.
        if fast:
            slow = slow.next

        reversed_list = reverse_linked_list(slow)

        cur1, cur2 = head, reversed_list
        while cur2:
            if cur1.val != cur2.val: return False
            cur1, cur2 = cur1.next, cur2.next

        return True





