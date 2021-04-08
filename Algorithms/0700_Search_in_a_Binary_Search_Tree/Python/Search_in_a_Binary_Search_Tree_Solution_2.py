
# Space: O(n)
# Time: O(1)

# Iterative approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None
        cur = root

        while cur:
            if cur.val == val:
                return cur
            if cur.val < val:
                cur = cur.right
            else:
                cur = cur.left
        return None



