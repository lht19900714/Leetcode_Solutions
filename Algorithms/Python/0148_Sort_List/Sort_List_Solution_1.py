
# Space: O(n)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import collections

class Solution:
    def sortList(self, head):
        if not head: return None
        if head.next is None: return head

        data = collections.defaultdict(list)

        # create a dict for sorting purpose
        cur = head
        while cur:
            data[cur.val].append(cur)
            cur = cur.next

        # sort dict.keys() to accomplish sorting requirement
        temp_list = list(data.keys())
        temp_list.sort()

        # build sorted linked list
        res = ListNode(-1)
        cur_res = res

        for i in temp_list:
            for j in data[i]:
                cur_res.next = j
                cur_res = cur_res.next

        cur_res.next = None

        return res.next





