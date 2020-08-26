
# Space: O(1)
# Time: O(n)

# Iterative approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def mergeTwoLists(self, l1, l2):

        res = ListNode(0)

        cur_res = res
        cur1, cur2 = l1,l2

        while cur1 and cur2:
            if cur1.val<cur2.val:
                cur_res.next = cur1
                cur1 = cur1.next
                cur_res = cur_res.next
            else:
                cur_res.next = cur2
                cur2 = cur2.next
                cur_res = cur_res.next

        if cur1:
            cur_res.next = cur1
        else:
            cur_res.next = cur2

        return res.next




