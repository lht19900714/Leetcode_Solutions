
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if root is None: return True
        if root.left is None and root.right is None: return True

        def helper(r1, r2):
            if r1 is None and r2 is None: return True
            if (r1 is None and r2 is not None) or (r1 is not None and r2 is None): return False
            if r1.val != r2.val: return False
            if r1.left is None and r1.right is None and r2.left is None and r2.right is None and r1.val == r2.val: return True

            return helper(r1.left, r2.right) and helper(r1.right, r2.left)

        return helper(root, root)




