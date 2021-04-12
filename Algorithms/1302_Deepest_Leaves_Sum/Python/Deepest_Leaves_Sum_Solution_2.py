
# Space: O(1)
# Time: O(n)

# DFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root):
        if root is None: return 0
        if root.left is None and root.right is None: return root.val
        self.res, self.deepest_level = 0, 0

        def dfs(node, level):
            if node.left is None and node.right is None:
                if level == self.deepest_level:
                    self.res += node.val
                elif level > self.deepest_level:
                    self.res = node.val
                    self.deepest_level = level
                return

            if node.left: dfs(node.left, level + 1)
            if node.right: dfs(node.right, level + 1)

        dfs(root, 0)
        return self.res





