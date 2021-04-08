
# Space: O(n)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists):
        length = len(lists)
        if length == 0: return None
        if length == 1: return lists[0]

        res = ListNode()
        cur_res = res

        cache = []
        for head in lists:
            while head:
                cache.append(head.val)
                head = head.next

        cache.sort()
        for val in cache:
            cur_res.next = ListNode(val)
            cur_res = cur_res.next

        return res.next






