
# Space: O(n)
# Time: O(1)

# Recursive approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None

        def recursive(root, val):
            if root is None: return None
            if root.val == val: return root
            if root.val > val: return recursive(root.left, val)
            if root.val < val: return recursive(root.right, val)

        return recursive(root, val)











