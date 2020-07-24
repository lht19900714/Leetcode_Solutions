
# Space: O(n)
# Time: O(n)

# BFS solution

class Solution:
    def allPathsSourceTarget(self, graph):
        res = []
        queue = [[[0], graph[0]]]

        while queue:
            path, cur_node_list = queue.pop(0)
            if len(cur_node_list) == 0:
                res.append(path)
            for i in cur_node_list:
                queue.append([path + [i], graph[i]])

        return res





