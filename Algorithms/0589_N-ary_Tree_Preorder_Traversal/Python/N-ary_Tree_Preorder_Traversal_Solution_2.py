
# Space: O(1)
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

        def dfs(root):
            if root is None: return []
            if root.children is None: return [root.val]
            res = [root.val]
            for c in root.children:
                res += dfs(c)
            return res

        return dfs(root)










