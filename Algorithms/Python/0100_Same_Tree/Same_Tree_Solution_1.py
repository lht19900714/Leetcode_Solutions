
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        queue = [[p, q]]
        while queue:
            cur_p, cur_q = queue.pop(0)
            if cur_p is None and cur_q is None:
                continue
            if cur_p is None or cur_q is None:
                return False
            if cur_p.val != cur_q.val:
                return False
            queue.append([cur_p.left, cur_q.left])
            queue.append([cur_p.right, cur_q.right])
        return True
