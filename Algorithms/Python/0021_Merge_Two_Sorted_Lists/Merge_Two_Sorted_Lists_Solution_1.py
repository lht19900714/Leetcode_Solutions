
# Space: O(1)
# Time: O(n)

# Recursive approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def mergeTwoLists(self, l1, l2):
        def helper(l1, l2):

            if l1 is None and l2 is None: return None
            if l1 is None: return l2
            if l2 is None: return l1

            res = ListNode(0)

            if l1.val < l2.val:
                l1.next = helper(l1.next, l2)
                res.next = l1
            else:
                l2.next = helper(l1, l2.next)
                res.next = l2

            return res.next

        return helper(l1, l2)



