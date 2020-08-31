
# Space: O(1)
# Time: O(logn)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root, key):
        if root is None: return None
        if self.search(root, key):
            return self.delete(root, key)
        return root

    def delete(self, root, target):
        if root.val > target:
            root.left = self.delete(root.left, target)
        elif root.val < target:
            root.right = self.delete(root.right, target)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.min_node(root.right)
                root.val = successor.val
                root.right = self.delete(root.right, successor.val)
        return root

    def search(self, root, target):
        if root is None: return False
        cur = root
        while cur:
            if cur.val == target:
                return True
            elif cur.val > target:
                cur = cur.left
            elif cur.val < target:
                cur = cur.right
        return False

    def min_node(self, root):
        if root is None: return None
        cur = root
        while cur.left:
            cur = cur.left
        return cur
