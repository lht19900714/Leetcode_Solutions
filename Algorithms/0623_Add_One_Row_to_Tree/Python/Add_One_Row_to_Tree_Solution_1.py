
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def addOneRow(self, root, v, d):
        if d==1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node

        def helper(root, cur_level, required_level, required_val, direction):
            if root is None and cur_level == required_level:
                new_node = TreeNode(required_val)
                return new_node

            if root is None: return root

            if cur_level == required_level:
                new_node = TreeNode(required_val)
                if direction == 'left':
                    new_node.left = root
                if direction == 'right':
                    new_node.right = root
                return new_node

            root.left = helper(root.left, cur_level + 1, required_level, required_val, 'left')
            root.right = helper(root.right, cur_level + 1, required_level, required_val, 'right')

            return root

        return helper(root, 1, d, v, '')




