
# Space: O(n)
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head):
        if head is None: return None
        if head.next is None: return TreeNode(head.val)
        cache = []
        pointer = head
        while pointer:
            cache.append(pointer.val)
            pointer = pointer.next

        def build_tree(alist):
            if len(alist) == 0: return None
            if len(alist) == 1: return TreeNode(alist[0])
            mid = len(alist) // 2
            head = TreeNode(alist[mid])
            left = alist[:mid]
            right = alist[mid + 1:]
            head.left = build_tree(left)
            head.right = build_tree(right)
            return head

        return build_tree(cache)




