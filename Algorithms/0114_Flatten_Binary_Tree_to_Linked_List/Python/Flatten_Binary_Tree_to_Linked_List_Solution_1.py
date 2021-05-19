
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None: return
        if root.left is None and root.right is None: return
        stack = [root]

        while stack:
            cur = stack.pop()
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
            if stack: cur.right = stack[-1]
            cur.left = None




