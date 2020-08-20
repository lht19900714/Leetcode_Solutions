
# Space: O(n)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None: return None
        if head.next is None: return head

        data = {}
        index = 0
        cur = head
        # using dict to create a index for each node
        while cur:
            data[index] = cur
            index += 1
            cur = cur.next

        # create a flag to handle odd/even nodes situation
        odd_nodes = False if index % 2 == 0 else True

        front, end = 0, len(data) - 1
        res = ListNode()
        res_pointer = res

        while front < end:
            res_pointer.next = data[front]
            res_pointer = res_pointer.next
            res_pointer.next = data[end]
            res_pointer = res_pointer.next
            front += 1
            end -= 1

        if odd_nodes:
            res_pointer.next = data[front]
            res_pointer = res_pointer.next
        res_pointer.next = None

        return res.next




