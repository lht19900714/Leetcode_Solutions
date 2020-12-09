
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.res = None

        def recursion(root):
            if root is None: return False

            left = recursion(root.left)
            right = recursion(root.right)

            mid = True if root == p or root == q else False

            if mid + left + right > 1: self.res = root

            return mid or left or right

        recursion(root)
        return self.res






