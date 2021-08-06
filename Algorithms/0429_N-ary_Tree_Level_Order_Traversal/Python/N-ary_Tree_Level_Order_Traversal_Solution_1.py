
# Space: O(n)
# Time: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


class Solution:
    def levelOrder(self, root):
        if root is None: return []
        res = collections.defaultdict(list)
        res_list = []

        queue = [[0, root]]
        while queue:
            cur_level, cur_root = queue.pop(0)
            res[cur_level].append(cur_root.val)
            if cur_root.children:
                for each_child in cur_root.children:
                    queue.append([cur_level + 1, each_child])

        for i in range(len(res)):
            res_list.append(res[i])
        return [res[i] for i in range(len(res))]




