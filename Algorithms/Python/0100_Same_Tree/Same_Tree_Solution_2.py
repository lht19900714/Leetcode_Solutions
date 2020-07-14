
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def pre_order_traversal(node):
            if node is None:
                return [None]
            res = []
            res.append(node.val)
            res += pre_order_traversal(node.left)
            res += pre_order_traversal(node.right)
            return res

        def in_order_traversal(node):
            if node is None:
                return [None]
            res = []
            res += in_order_traversal(node.left)
            res.append(node.val)
            res += in_order_traversal(node.right)
            return res

        return pre_order_traversal(p) == pre_order_traversal(q) and in_order_traversal(p) == in_order_traversal(q)
