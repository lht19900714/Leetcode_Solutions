
# Space: O(1)
# Time: O(n^2)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertionSortList(self, head):
        if head is None or head.next is None: return head

        cur, prev = head.next, head

        while cur:
            temp_prev, temp_head = None, head

            while temp_head != cur:
                if temp_head.val > cur.val:
                    if temp_prev:
                        temp_prev.next = cur
                    else:
                        temp_prev = cur
                        head = temp_prev

                    prev.next = cur.next
                    cur.next = temp_head
                    cur = prev.next
                    break

                temp_prev = temp_head
                temp_head = temp_head.next

            else:
                prev = cur
                cur = cur.next

        return head





