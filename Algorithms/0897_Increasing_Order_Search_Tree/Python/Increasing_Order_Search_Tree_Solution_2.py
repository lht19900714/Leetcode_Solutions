
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root):
        if root is None: return root
        if root.left is None and root.right is None: return root

        # inorder_traversal_generator
        def inorder_traversal(root):
            if root:
                yield from inorder_traversal(root.left)
                yield root.val
                yield from inorder_traversal(root.right)

        res = TreeNode()
        cur_res = res

        # restructure tree
        for i in inorder_traversal(root):
            cur_res.right = TreeNode(i)
            cur_res = cur_res.right

        return res.right




