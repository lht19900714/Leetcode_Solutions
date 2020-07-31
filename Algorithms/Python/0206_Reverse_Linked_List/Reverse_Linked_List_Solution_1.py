
# Space: O(1)
# Time: O(n)

# iterative approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        previous, current = None, head

        while current:
            current.next, previous, current = previous, current, current.next

        return previous


