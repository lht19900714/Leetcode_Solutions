
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root):
        self.cache = {}
        queue = [[root, 0]]
        max_deep = 0

        while queue:
            cur_node, cur_level = queue.pop(0)
            self.cache[cur_node] = cur_level
            if cur_node.left:
                queue.append([cur_node.left, cur_level + 1])
            if cur_node.right:
                queue.append([cur_node.right, cur_level + 1])

            max_deep = max(max_deep, cur_level)

        def helper(root):
            if not root or self.cache[root] == max_deep:
                return root

            left = helper(root.left)
            right = helper(root.right)

            return root if left and right else left or right

        return helper(root)




