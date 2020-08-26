
# Space: O(1)
# Time: O(n)

# Recursive approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.cache = {}

        def helper(root, level):
            if root is None: return 0
            if root.left is None and root.right is None: return level + 1
            if root in self.cache: return self.cache[root]

            res = max(helper(root.left, level + 1), helper(root.right, level + 1))
            self.cache[root] = res
            return res

        return helper(root, 0)



