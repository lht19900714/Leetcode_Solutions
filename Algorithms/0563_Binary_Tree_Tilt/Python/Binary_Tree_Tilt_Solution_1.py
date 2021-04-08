
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root):
        if root is None: return 0
        if root.left is None and root.right is None: return 0

        self.res = 0

        def helper(root):
            if root is None: return 0

            head = root.val
            left = helper(root.left)
            right = helper(root.right)

            self.res += abs(left - right)
            return head + left + right

        helper(root)
        return self.res




