
# Space: O(n)
# Time: O(n)

# Solution with collections library


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution():
    def zigzagLevelOrder(self, root):

        if root is None: return []

        data = collections.defaultdict(list)
        queue = [[root, 0]]
        res = []

        while queue:
            cur_root, cur_level = queue.pop(0)
            data[cur_level].append(cur_root.val)
            if cur_root.left: queue.append([cur_root.left, cur_level + 1])
            if cur_root.right: queue.append([cur_root.right, cur_level + 1])

        for i in range(len(data)):
            if i % 2 == 0:
                res.append(data[i])
            else:
                res.append(data[i][::-1])

        return res

