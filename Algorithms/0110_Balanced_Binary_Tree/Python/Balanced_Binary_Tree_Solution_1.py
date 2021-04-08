
# Space: O(1)
# Time: O(nlogn)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        if root is None: return True
        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    def height(self, root):
        if root is None: return 0

        left = self.height(root.left)
        right = self.height(root.right)

        return max(left, right) + 1





