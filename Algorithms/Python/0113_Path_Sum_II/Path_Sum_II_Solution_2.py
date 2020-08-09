# Space: O(n)
# Time: O(n)

# BFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root, s):
        if root is None: return []
        res, path = [], []

        queue = [[root, path]]

        while queue:
            cur_root, cur_path = queue.pop(0)
            if cur_root.left is None and cur_root.right is None and s == sum(cur_path) + cur_root.val:
                res.append(cur_path + [cur_root.val])

            if cur_root.left:
                queue.append([cur_root.left, cur_path + [cur_root.val]])
            if cur_root.right:
                queue.append([cur_root.right, cur_path + [cur_root.val]])

        return res



