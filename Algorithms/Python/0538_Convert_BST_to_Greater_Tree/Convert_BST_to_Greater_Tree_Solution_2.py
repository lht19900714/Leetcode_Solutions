
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root):
        if (root is None) or (root.left is None and root.right is None): return root

        self.total = 0

        def recursive(root):
            if root is not None:
                recursive(root.right)
                self.total += root.val
                root.val = self.total
                recursive(root.left)
            return root

        return recursive(root)




