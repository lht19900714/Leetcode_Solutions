
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        if root is None: return True

        self.flag = True

        def height(root):
            if root is None or self.flag is False: return -1
            left = height(root.left)
            right = height(root.right)
            if abs(left - right) > 1:
                self.flag = False
                return -1
            return max(left, right) + 1

        height(root)
        return self.flag





