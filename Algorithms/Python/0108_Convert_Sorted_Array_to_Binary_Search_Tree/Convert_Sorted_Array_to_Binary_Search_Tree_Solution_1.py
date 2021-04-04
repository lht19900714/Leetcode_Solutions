
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        length = len(nums)
        if length == 1: return TreeNode(nums[0])

        def build_tree(alist):
            length = len(alist)
            if length == 1: return TreeNode(alist[0])

            mid = length // 2
            root = TreeNode(alist[mid])

            left_alist = alist[0:mid]
            right_alist = alist[mid + 1:]

            left = build_tree(left_alist) if left_alist else None
            right = build_tree(right_alist) if right_alist else None

            root.left = left
            root.right = right

            return root

        return build_tree(nums)





