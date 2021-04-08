
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trimBST(self, root, low, high):
        if root is None: return root
        if root.left is None and root.right is None and low <= root.val <= high: return root

        def trim(node, low, high):
            if node is None: return node
            if node.val < low: return trim(node.right, low, high)
            if node.val > high: return trim(node.left, low, high)
            if low <= node.val <= high:
                node.left = trim(node.left, low, high)
                node.right = trim(node.right, low, high)
                return node

        return trim(root, low, high)




                                                                                               