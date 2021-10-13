
# Space: O(1)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        return self.dfs(preorder)

    def dfs(self, alist):
        if len(alist) == 0: return None
        if len(alist) == 1: return TreeNode(alist[0])
        root = TreeNode(alist[0])
        index = 1
        left, right = [], []
        while index < len(alist):
            if alist[index] < alist[0]:
                left.append(alist[index])
                index += 1
            else:
                break
        right = alist[index:]
        root.left = self.dfs(left)
        root.right = self.dfs(right)
        return root




