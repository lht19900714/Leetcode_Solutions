
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root):

        def inorder_traversal(root):
            if root is None: return []
            res = []
            res += inorder_traversal(root.left)
            res.append(root.val)
            res += inorder_traversal(root.right)
            return res

        self.cache = inorder_traversal(root)
        self.length = len(self.cache)

    def next(self) -> int:
        self.length -= 1
        return self.cache.pop(0)

    def hasNext(self) -> bool:
        return True if self.length > 0 else False





