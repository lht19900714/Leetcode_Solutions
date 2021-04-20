
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
    def postorder(self, root):
        if root is None: return []
        if root.children is None: return root.val

        stack, res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.children:
                stack += cur.children

        return res[::-1]




