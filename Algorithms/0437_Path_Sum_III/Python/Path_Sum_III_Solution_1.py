
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
    def pathSum(self, root, sum):

        def bfs(root, target):
            if root is None: return 0
            queue = [[root, target]]
            count = 0

            while queue:
                cur_root, cur_target = queue.pop(0)
                if cur_root.val == cur_target: count += 1
                if cur_root.left:
                    queue.append([cur_root.left, cur_target - cur_root.val])
                if cur_root.right:
                    queue.append([cur_root.right, cur_target - cur_root.val])
            return count

        if root is None: return 0
        return bfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


