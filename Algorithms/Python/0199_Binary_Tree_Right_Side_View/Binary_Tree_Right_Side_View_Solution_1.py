
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        if root is None: return []
        if root.left is None and root.right is None: return [root.val]

        res = {}
        level = 0
        queue = [[level, root]]

        while queue:
            cur_level, cur_root = queue.pop(0)
            res[cur_level] = cur_root.val
            if cur_root.left: queue.append([cur_level+1,cur_root.left])
            if cur_root.right: queue.append([cur_level+1,cur_root.right])

        return res.values()




