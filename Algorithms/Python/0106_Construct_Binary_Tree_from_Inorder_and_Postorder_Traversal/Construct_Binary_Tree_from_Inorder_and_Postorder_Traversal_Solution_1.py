
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None

        root_value = postorder.pop()
        root = TreeNode(root_value)
        root_index_in_inorder = inorder.index(root_value)

        # CAUTION: we need to recursively build right node first.
        #          since we pop item from end of postorder list, so we will get right node first, then left node.
        root.right = self.buildTree(inorder[root_index_in_inorder + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index_in_inorder], postorder)

        return root



