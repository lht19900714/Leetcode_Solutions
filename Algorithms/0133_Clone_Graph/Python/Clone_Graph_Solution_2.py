
# Space: O(n)
# Time: O(n)

# DFS Approach

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return None

        self.node_dict = {}

        def dfs(node):
            if node in self.node_dict: return self.node_dict[node]

            self.node_dict[node] = Node(node.val)

            for neighbor in node.neighbors:
                self.node_dict[node].neighbors.append(dfs(neighbor))

            return self.node_dict[node]

        dfs(node)
        return self.node_dict[node]




