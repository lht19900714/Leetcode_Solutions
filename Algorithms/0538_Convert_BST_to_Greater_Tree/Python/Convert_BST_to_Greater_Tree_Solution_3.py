
# Space: O(n)
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

        total = 0
        cur_root = root
        stack = []

        while stack or cur_root:
            while cur_root:
                stack.append(cur_root)
                cur_root = cur_root.right

            cur_root = stack.pop()
            total += cur_root.val
            cur_root.val = total
            cur_root = cur_root.left

        return root





