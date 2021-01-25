
# Space: O(n)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists):
        length = len(lists)
        if length == 0: return None
        if length == 1: return lists[0]

        res = ListNode()
        cur_res = res

        while len(lists) > 1:
            min_index, cur_index, min_value = 0, 0, float('inf')
            while cur_index < len(lists):
                if not lists[cur_index]:
                    lists.pop(cur_index)
                    continue
                if lists[cur_index].val < min_value:
                    min_index = cur_index
                    min_value = lists[cur_index].val

                cur_index += 1

            if min_index < len(lists) and lists[min_index]:
                cur_res.next = lists[min_index]
                cur_res = cur_res.next
                lists[min_index] = lists[min_index].next

        cur_res.next = lists[0] if lists else None

        return res.next




