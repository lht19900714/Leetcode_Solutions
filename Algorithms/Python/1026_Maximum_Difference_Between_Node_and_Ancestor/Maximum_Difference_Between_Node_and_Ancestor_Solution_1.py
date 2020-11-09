
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root):
        self.res = 0

        def helper(root):
            if not root: return []

            head = root.val
            left = helper(root.left)
            right = helper(root.right)

            if left:
                max_left, min_left = max(left), min(left)
                self.res = max(self.res, abs(head - max_left), abs(head - min_left))
            if right:
                max_right, min_right = max(right), min(right)
                self.res = max(self.res, abs(head - max_right), abs(head - min_right))

            return [head] + left + right

        helper(root)
        return self.res



