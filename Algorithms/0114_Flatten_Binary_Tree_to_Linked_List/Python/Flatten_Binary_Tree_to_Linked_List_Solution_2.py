
# Space: O(1)
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

        def dfs(root):
            if root is None: return None
            leftlast = dfs(root.left)
            rightlast = dfs(root.right)

            if leftlast is not None:
                leftlast.right = root.right
                root.right = root.left
                root.left = None

            if rightlast: return rightlast
            if leftlast: return leftlast
            return root

        dfs(root)




