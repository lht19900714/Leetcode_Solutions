
# Space: O(n)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head):
        if not head: return True
        if head.next is None: return True

        temp = []
        while head:
            temp.append(head.val)
            head = head.next

        return True if temp == temp[::-1] else False




