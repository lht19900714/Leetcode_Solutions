
# Space: O(1)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None: return head

        res = ListNode()
        cur_res = res
        prev_val = None

        cur = head

        while cur:

            if cur.next:
                if cur.val != cur.next.val and cur.val != prev_val:
                    cur_res.next = cur
                    cur_res = cur_res.next
            elif not cur.next:
                if cur.val != prev_val:
                    cur_res.next = cur
                    cur_res = cur_res.next

            prev_val = cur.val
            cur = cur.next

        cur_res.next = None

        return res.next




