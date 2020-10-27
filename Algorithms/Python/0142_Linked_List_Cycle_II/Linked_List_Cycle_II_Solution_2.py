
# Space: O(1)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if head is None or head.next is None: return None

        fast, slow = head, head

        # detect if cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        # find the beginning of the cycle.
        cur = head

        while cur != fast:
            cur = cur.next
            fast = fast.next

        return cur



