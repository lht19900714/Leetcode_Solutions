
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

        last_added_value = None
        res = ListNode()
        cur_res = res
        cur = head

        while cur:
            if cur.val != last_added_value:
                cur_res.next = cur
                last_added_value = cur.val
                cur_res = cur_res.next
            cur = cur.next

        cur_res.next = None

        return res.next






