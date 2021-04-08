
# Space: O(1)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapNodes(self, head, k):
        if head is None or head.next is None: return head

        begin, end = None, None
        length = 0
        cur = head

        # find begin node
        while cur:
            length += 1
            if length == k:
                begin = cur
            cur = cur.next

        # find end node
        counter = 1
        cur = head
        while counter != length - k + 1:
            cur = cur.next
            counter += 1
        end = cur

        begin.val, end.val = end.val, begin.val

        return head






