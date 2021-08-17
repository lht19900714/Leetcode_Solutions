
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):
        if root is None: return 0
        if root.left is None and root.right is None: return 1
        self.count = 0

        def dfs(root, point):
            if root is None: return
            if root.val >= point: self.count += 1

            if root.left:
                dfs(root.left, max(point, root.val))
            if root.right:
                dfs(root.right, max(point, root.val))

        dfs(root,root.val)
        return self.count




