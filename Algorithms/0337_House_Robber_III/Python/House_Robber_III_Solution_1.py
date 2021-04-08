
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root):
        if root is None: return 0
        if root.left is None and root.right is None: return root.val
        self.memory = {}

        def helper(node, flag):  # flag == 1: can be selected; flag == 0: can not be selected
            if node is None: return 0
            if node.left is None and node.right is None and flag == 1: return node.val
            if node.left is None and node.right is None and flag == 0: return 0

            if (node, flag) in self.memory: return self.memory[(node, flag)]

            if flag == 1:
                temp_res_1 = node.val + helper(node.left, 0) + helper(node.right, 0)
                temp_res_2 = helper(node.left, 1) + helper(node.right, 1)
                res = max(temp_res_1, temp_res_2)

            if flag == 0:
                res = helper(node.left, 1) + helper(node.right, 1)

            self.memory[(node, flag)] = res
            return res

        return helper(root, 1)




