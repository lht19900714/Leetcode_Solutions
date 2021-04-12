
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
    def deepestLeavesSum(self, root):
        if root is None: return 0
        if root.left is None and root.right is None: return root.val
        queue = [[root, 0]]
        res, deepest_level = 0, 0
        while queue:
            cur_root, cur_level = queue.pop(0)
            if cur_root.left is None and cur_root.right is None:
                if cur_level == deepest_level:
                    res += cur_root.val
                elif cur_level> deepest_level:
                    res = cur_root.val
                    deepest_level = cur_level

            if cur_root.left: queue.append([cur_root.left,cur_level+1])
            if cur_root.right: queue.append([cur_root.right,cur_level+1])

        return res





