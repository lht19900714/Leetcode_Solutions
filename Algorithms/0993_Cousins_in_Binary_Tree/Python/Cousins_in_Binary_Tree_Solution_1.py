
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root, x, y):
        x_level, y_level, x_parent, y_parent = -1, -1, None, None
        queue = [[root, 0, None]]
        while queue:
            cur_root, cur_level, cur_parent = queue.pop(0)
            if cur_root.val == x:
                x_level = cur_level
                x_parent = cur_parent
            if cur_root.val == y:
                y_level = cur_level
                y_parent = cur_parent
            if x_level != -1 and y_level != -1:
                return x_level == y_level and x_parent != y_parent
            if cur_root.left: queue.append([cur_root.left, cur_level + 1, cur_root])
            if cur_root.right: queue.append([cur_root.right, cur_level + 1, cur_root])
        return False





