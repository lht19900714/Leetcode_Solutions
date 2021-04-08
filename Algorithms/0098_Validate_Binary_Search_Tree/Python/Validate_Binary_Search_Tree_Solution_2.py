
# Space: O(1)
# Time: O(n)

# Iterative approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        if root is None: return True
        if root.left is None and root.right is None: return True

        left_value, right_value = -float('inf'), float('inf')
        queue = [[root, left_value, right_value]]
        while queue:
            cur, cur_left, cur_right = queue.pop(0)
            if not cur_left < cur.val < cur_right: return False
            if cur.left:
                queue.append([cur.left, cur_left, cur.val])
            if cur.right:
                queue.append([cur.right, cur.val, cur_right])
        return True






                                                                                                                              