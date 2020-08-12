
# Space: O(1)
# Time: O(n)

# iterative approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        res = ListNode()  # result anchor
        previous_node = res

        while head and head.next:
            first_node = head
            second_node = head.next

            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            previous_node = first_node
            head = head.next

        return res.next


