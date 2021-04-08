
# Space: O(1)
# Time: O(n)

# Recursive approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        if root is None: return True
        if root.left is None and root.right is None: return True

        def helper(root, left, right):
            if root is None: return True
            if not left < root.val < right: return False
            if not helper(root.left, left, root.val): return False
            if not helper(root.right, root.val, right): return False
            return True

        return helper(root, -float('inf'), float('inf'))
