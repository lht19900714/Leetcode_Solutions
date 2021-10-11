
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None: return 0
        left, right = 0, 0
        if root.left:
            left = self.dfs(root.left) + 1
        if root.right:
            right = self.dfs(root.right) + 1
        self.res = max(self.res, left + right)
        return max(left, right)





