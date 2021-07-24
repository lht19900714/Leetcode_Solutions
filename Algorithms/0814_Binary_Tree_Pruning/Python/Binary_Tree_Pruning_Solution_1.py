
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root):
        if root is None: return root
        if root.left is None and root.right is None:
            if root.val == 0: return None
            return root

        def dfs(root):
            if root is None: return 0
            if root.left is None and root.right is None: return root.val

            left = dfs(root.left)
            right = dfs(root.right)

            if left == 0: root.left = None
            if right == 0: root.right = None
            if left == 0 and right == 0 and root.val == 0: return 0
            return 1

        res = dfs(root)
        return root if res != 0 else None




