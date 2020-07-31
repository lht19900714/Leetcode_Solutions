
# Space: O(1)
# Time: O(n)

# recursive approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):

        def recursive(root):
            if root is None or root.next is None:
                return root

            root_next = recursive(root.next)
            root.next.next = root
            root.next = None

            return root_next

        return recursive(head)




