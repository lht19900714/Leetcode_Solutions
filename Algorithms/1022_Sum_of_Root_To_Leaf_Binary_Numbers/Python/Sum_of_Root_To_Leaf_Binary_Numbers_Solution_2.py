
# Space: O(1)
# Time: O(n)

# BFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root):
        if root.left is None and root.right is None: return root.val
        self.res = 0

        def helper(root, temp_res):
            if root.left is None and root.right is None:
                self.res += int(temp_res + str(root.val), 2)
                return

            if root.left: helper(root.left, temp_res + str(root.val))
            if root.right: helper(root.right, temp_res + str(root.val))

        helper(root,'')

        return self.res






