
# Time:  O(p + r * n), p is the count of all the possible paths in graph,
#                      r is the count of the result.
# Space: O(n)

# DFS solution

class Solution:
    def allPathsSourceTarget(self, graph):
        res = []
        length = len(graph)

        def dfs(node, graph, path):
            if node == length - 1:
                res.append(path[:])
                return

            for i in graph[node]:
                path.append(i)
                dfs(i, graph, path)
                path.pop()

        dfs(0, graph, [0])

        return res


