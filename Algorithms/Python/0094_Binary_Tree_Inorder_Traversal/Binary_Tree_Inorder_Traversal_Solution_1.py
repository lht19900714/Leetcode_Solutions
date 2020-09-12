
# Space: O(n)
# Time: O(n)

# Recursive approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):
        if root is None: return []
        if root.left is None and root.right is None: return [root.val]

        def inorder(root):
            if root is None: return []
            res = []

            res += inorder(root.left)
            res.append(root.val)
            res += inorder(root.right)

            return res

        return inorder(root)




