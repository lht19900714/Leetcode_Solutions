
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1, root2):
        res = self.get_element(root1) + self.get_element(root2)
        res.sort()
        return res

    def get_element(self, root):  # standard level traversal to get all elements from a tree
        if root is None: return []
        res = []
        queue = [root]
        while queue:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
        return res




