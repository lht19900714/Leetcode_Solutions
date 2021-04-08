
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution:
    def verticalTraversal(self, root):
        data = collections.defaultdict(list)

        x, y = 0, 0
        queue = [[root, x, y]]

        # tag x, y coordinates for each node
        while queue:
            cur_root, cur_x, cur_y = queue.pop(0)
            data[(cur_x, cur_y)].append(cur_root.val)
            data[(cur_x, cur_y)].sort()
            if cur_root.left:
                queue.append([cur_root.left, cur_x - 1, cur_y - 1])
            if cur_root.right:
                queue.append([cur_root.right, cur_x + 1, cur_y - 1])

        # sort dictionary key as requirement
        sorted_key = sorted(data.keys(), key=lambda x: (x[0], -x[1]))

        # build result
        res_dict = collections.defaultdict(list)
        for i in sorted_key:
            res_dict[i[0]] += data[i]

        return res_dict.values()



