
# Space: O(n)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1

        reversed_l1 = self.reverse_list(l1)
        reversed_l2 = self.reverse_list(l2)
        res = ListNode()
        carry_forward = 0
        pointer_1, pointer_2, pointer_res = reversed_l1, reversed_l2, res

        while pointer_1 or pointer_2 or carry_forward:

            value_1 = pointer_1.val if pointer_1 else 0
            value_2 = pointer_2.val if pointer_2 else 0

            value = value_1 + value_2 + carry_forward

            if value >= 10:
                carry_forward = 1
                pointer_res.next = ListNode(value % 10)
            else:
                carry_forward = 0
                pointer_res.next = ListNode(value)


            if pointer_1: pointer_1 = pointer_1.next
            if pointer_2: pointer_2 = pointer_2.next

            pointer_res = pointer_res.next

        return self.reverse_list(res.next)

    def reverse_list(self, head):
        if head is None or head.next is None:
            return head
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
