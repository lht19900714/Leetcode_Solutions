
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None

        root_value = preorder.pop(0)
        root = TreeNode(root_value)
        root_index_in_preorder = inorder.index(root_value)

        root.left = self.buildTree(preorder, inorder[:root_index_in_preorder])
        root.right = self.buildTree(preorder, inorder[root_index_in_preorder + 1:])

        return root



