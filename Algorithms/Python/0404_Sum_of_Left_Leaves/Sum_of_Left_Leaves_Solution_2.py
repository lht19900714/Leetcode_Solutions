
# Space: O(n)
# Time: O(n)

# DFS approach(iterative)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None: return 0

        stack = []
        flag = False  # indicate if this node from left leaf
        cur = (root, flag)
        res = 0

        while stack or cur[0]:

            while cur[0]:
                stack.append(cur)
                cur = (cur[0].left, True)
            cur = stack.pop()

            if cur[0].left is None and cur[0].right is None and cur[1] is True:
                res += cur[0].val

            cur = (cur[0].right, False)
        return res



