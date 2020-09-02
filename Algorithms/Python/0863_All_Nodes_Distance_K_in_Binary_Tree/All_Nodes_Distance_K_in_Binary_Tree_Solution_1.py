
# Space: O(n)
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def distanceK(self, root, target, K):
        self.graph = collections.defaultdict(list)
        self.visited = set()
        res = []

        def build_graph(parent_node, child_node):  # build a undirected graph
            if parent_node:
                self.graph[parent_node.val].append(child_node.val)
                self.graph[child_node.val].append(parent_node.val)

            if child_node.left: build_graph(child_node, child_node.left)
            if child_node.right: build_graph(child_node, child_node.right)

        build_graph(None, root)

        step = 0
        queue = [[target.val, step]]
        self.visited.add(target.val)

        # BFS approach to find K distince node
        while queue and step <= K:
            cur_queue_length = len(queue)
            while cur_queue_length:
                cur_node, cur_step = queue.pop(0)
                if cur_step == K: res.append(cur_node)
                for each in self.graph[cur_node]:
                    if each not in self.visited:
                        queue.append([each, step + 1])
                        self.visited.add(each)
                cur_queue_length -= 1
            step += 1
        return res



