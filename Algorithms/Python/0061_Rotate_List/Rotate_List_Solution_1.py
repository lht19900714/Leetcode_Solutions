
# Space: O(1)
# Time: O(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        if head is None or k == 0: return head

        res_header = ListNode(0)
        last_node = None
        length = 0
        temp = head

        # loop through linked list to get the length and last_node, these will be used for rotation.
        while temp:
            if temp.next is None: last_node = temp
            temp = temp.next
            length += 1

        if length == 1: return head

        # calculate new header's index
        new_header_index = length - (k % length)
        if new_header_index == length: return head

        # loop through linked list again to find rotation point and re-construct linked list
        cur, prev, count = head, None, 0
        while count != new_header_index:
            prev = cur
            cur = cur.next
            count += 1

        res_header.next = cur
        last_node.next = head
        prev.next = None

        return res_header.next



