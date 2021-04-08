
# Space: O(n)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import collections

class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None: return head

        res = ListNode()
        cur_res = res
        cache = collections.defaultdict(int)
        cur = head

        while cur:
            cache[cur.val] += 1
            cur = cur.next

        cur = head

        while cur:
            if cache[cur.val] == 1:
                cur_res.next = cur
                cur_res = cur_res.next
            cur = cur.next

        cur_res.next = None

        return res.next














