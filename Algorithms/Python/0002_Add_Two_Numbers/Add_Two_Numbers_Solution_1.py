
# Space: O(n)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1

        res = ListNode(0)
        carry_forward = 0
        pointer_1, pointer_2, pointer_res = l1, l2, res

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

        return res.next


