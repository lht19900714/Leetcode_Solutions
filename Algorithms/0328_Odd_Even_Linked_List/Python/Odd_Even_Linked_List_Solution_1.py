
# Space: O(1)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None or head.next.next is None: return head

        odd_head, even_head = ListNode(0), ListNode(0)
        odd_cur, even_cur = odd_head, even_head
        flag = 1
        cur = head
        while cur:
            if flag % 2 == 1:
                odd_cur.next = cur
                odd_cur = odd_cur.next
            elif flag % 2 == 0:
                even_cur.next = cur
                even_cur = even_cur.next
            cur = cur.next
            flag += 1

        odd_cur.next = even_head.next
        even_cur.next = None

        return odd_head.next




