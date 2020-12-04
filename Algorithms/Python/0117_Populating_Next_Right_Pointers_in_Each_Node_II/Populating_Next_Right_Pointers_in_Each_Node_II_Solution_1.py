
# Space: O(1)
# Time: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

"""

class Solution:
    def connect(self, root):
        if root is None: return root
        if root.left is None and root.right is None: return root

        cur, head_node, next_node = root, None, None

        while cur:
            while cur:
                if cur.left:
                    if head_node is None:
                        head_node = cur.left
                        next_node = cur.left
                    else:
                        next_node.next = cur.left
                        next_node = next_node.next

                if cur.right:
                    if head_node is None:
                        head_node = cur.right
                        next_node = cur.right
                    else:
                        next_node.next = cur.right
                        next_node = next_node.next

                cur = cur.next

            cur = head_node
            head_node = None
            next_node = None

        return root




