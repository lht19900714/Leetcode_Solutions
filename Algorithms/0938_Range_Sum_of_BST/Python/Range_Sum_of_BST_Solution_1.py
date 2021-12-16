
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low, high):
        if root.left is None and root.right is None: return root.val
        res = 0
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if low<=cur.val<=high:
                res+=cur.val
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
        return res




