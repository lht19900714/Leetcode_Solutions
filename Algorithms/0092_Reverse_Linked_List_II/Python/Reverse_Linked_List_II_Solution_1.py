
# Space: O(n)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseBetween(self, head, left, right):
        if head is None or head.next is None: return head
        if left == right: return head
        first, first_prev, second, second_next = None, None, None, None
        count = 1
        cur = head
        while cur is not None:
            if count == left - 1: first_prev = cur
            if count == left: first = cur
            if count == right: second = cur
            if count == right + 1:
                second_next = cur
                break
            count += 1
            cur = cur.next

        second.next = None
        reversed_list = self.reverse_list(first)

        if first_prev: first_prev.next = reversed_list
        else: head = reversed_list

        if second_next:
            temp_cur = head
            while temp_cur.next:
                temp_cur = temp_cur.next
            temp_cur.next = second_next

        return head

    def reverse_list(self, head):
        if head is None: return None
        if head.next is None: return head
        prev = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return prev

    # def reverse_list1(self, head):
    #     if head is None: return None
    #     if head.next is None: return head
    #     prev, cur = None, head
    #     while cur:
    #         temp = cur.next
    #         prev = cur
    #         cur = temp
    #     return prev





