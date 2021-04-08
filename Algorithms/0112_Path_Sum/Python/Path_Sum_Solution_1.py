
# Space: O(1)
# Time: O(n)

# DFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum) -> bool:

        if root is None: return False

        if root.left is None and root.right is None and sum == root.val: return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)



