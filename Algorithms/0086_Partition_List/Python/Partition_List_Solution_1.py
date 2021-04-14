
# Space: O(1)
# Time: O(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head, x):
        if head is None or head.next is None: return head
        temp1, temp2 = ListNode(0), ListNode(0)
        pointer1, pointer2 = temp1, temp2
        cur = head

        while cur:
            if cur.val < x:
                pointer1.next = cur
                pointer1 = pointer1.next
            elif cur.val >= x:
                pointer2.next = cur
                pointer2 = pointer2.next
            cur = cur.next

        pointer1.next = temp2.next
        pointer2.next = None

        return temp1.next





