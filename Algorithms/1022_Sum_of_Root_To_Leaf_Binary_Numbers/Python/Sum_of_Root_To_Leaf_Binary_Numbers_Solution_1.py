
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
    def sumRootToLeaf(self, root):
        if root.left is None and root.right is None: return root.val

        res = 0
        queue = [[root, '']]

        while queue:
            cur_node, cur_res = queue.pop(0)

            if cur_node.left is None and cur_node.right is None:
                res += int(cur_res + str(cur_node.val), 2)
                continue

            if cur_node.left: queue.append([cur_node.left, cur_res + str(cur_node.val)])
            if cur_node.right: queue.append([cur_node.right, cur_res + str(cur_node.val)])

        return res




