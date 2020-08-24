
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
    def sumOfLeftLeaves(self, root):
        if root is None: return 0

        queue = [root]
        res = 0

        while queue:
            cur = queue.pop(0)

            if cur.left:
                if cur.left.left is None and cur.left.right is None: # verify if this is left leaf
                    res += cur.left.val
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)
        return res




