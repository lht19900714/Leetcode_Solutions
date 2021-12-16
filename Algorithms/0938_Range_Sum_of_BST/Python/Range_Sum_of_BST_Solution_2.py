# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low, high):
        if root.left is None and root.right is None: return root.val

        def dfs(root, low, high):
            if root is None: return 0

            if root.val < low:
                return dfs(root.right, low, high)
            if root.val > high:
                return dfs(root.left, low, high)

            return dfs(root.left, low, high) + root.val + dfs(root.right, low, high)

        return dfs(root, low, high)





                                                                                                