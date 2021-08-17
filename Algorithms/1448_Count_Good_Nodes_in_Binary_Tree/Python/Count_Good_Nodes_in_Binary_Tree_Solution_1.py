
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):
        if root is None: return 0
        if root.left is None and root.right is None: return 1
        count = 0
        queue = [[root, root.val]]
        while queue:
            cur_root, cur_val = queue.pop(0)
            if cur_root.val >= cur_val:
                count += 1
            if cur_root.left:
                queue.append([cur_root.left, max(cur_val, cur_root.val)])
            if cur_root.right:
                queue.append([cur_root.right, max(cur_val, cur_root.val)])
        return count




