
# Space: O(n)
# Time: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
        if root is None: return []
        if root.children is None: return root.val
        queue = [root]
        res = []
        while queue:
            cur_node = queue.pop(0)
            res.append(cur_node.val)
            if cur_node.children:
                queue = cur_node.children + queue

        return res





