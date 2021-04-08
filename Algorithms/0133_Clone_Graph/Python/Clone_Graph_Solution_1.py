
# Space: O(n)
# Time: O(n)

# BFS Approach

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

        node_dict = {}
        queue = [node]

        while queue:
            cur = queue.pop(0)

            if cur not in node_dict:
                node_dict[cur] = Node(cur.val)

            for neighbor in cur.neighbors:
                if neighbor not in node_dict:
                    node_dict[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                node_dict[cur].neighbors.append(node_dict[neighbor])

        return node_dict[node]





