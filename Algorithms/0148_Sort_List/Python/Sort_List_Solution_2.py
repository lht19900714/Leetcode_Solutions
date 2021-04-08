
# Space: O(1)
# Time: O(nlogn)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# implement sorting as Merge Sort

def sortList(self, head):
    if not head: return None
    if head.next is None: return head

    # split linked list to two parts
    cur, mid, mid_prev = head, head, None

    while cur:
        cur = cur.next.next
        mid_prev = mid
        mid = mid.next

    mid_prev.next = None
    left = self.sortList1(head)
    right = self.sortList1(mid)

    # start merging
    left_pointer, right_pointer = left, right
    res = ListNode(-1)
    res_pointer = res

    while left_pointer is not None and right_pointer is not None:
        if left_pointer.val < right_pointer.val:
            res_pointer.next = left_pointer
            left_pointer = left_pointer.next
        else:
            res_pointer.next = right_pointer
            right_pointer = right_pointer.next
        res_pointer = res_pointer.next

    res_pointer.next = left_pointer if left_pointer else right_pointer

    return res.next




