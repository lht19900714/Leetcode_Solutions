
# Space: O(1)
# Time: O(n)

# BFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum) -> bool:

        if root is None: return False

        queue = [[root, sum]]

        while queue:

            cur_root, cur_target = queue.pop(0)

            if cur_root.left is None and cur_root.right is None and cur_target == cur_root.val:
                return True

            if cur_root.left:
                queue.append([cur_root.left, cur_target - cur_root.val])
            if cur_root.right:
                queue.append([cur_root.right, cur_target - cur_root.val])

        return False



