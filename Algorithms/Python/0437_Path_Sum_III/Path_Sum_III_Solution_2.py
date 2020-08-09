
# Space: O(n)
# Time: O(n)

# DFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, sum):

        def dfs(root, target):
            if root is None: return 0

            count = 0

            if root.val == target: count = 1

            count += dfs(root.left, target - root.val)
            count += dfs(root.right, target - root.val)
            return count

        if root is None: return 0
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)



