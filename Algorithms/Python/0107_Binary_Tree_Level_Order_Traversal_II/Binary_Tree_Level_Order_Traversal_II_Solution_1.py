
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root):
        if root is None: return []
        if root.left is None and root.right is None: return [[root.val]]

        self.res = []
        queue = [root]

        while queue:
            length = len(queue)
            temp_res = []

            while length:
                cur = queue.pop(0)
                temp_res.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                length -= 1

            self.res.append(temp_res)

        return self.res[::-1]





