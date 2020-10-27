
# Space: O(n)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if head is None or head.next is None: return None

        data = {}

        cur = head
        while cur:
            if cur in data: return cur

            data[cur] = cur.val
            cur = cur.next

        return None





