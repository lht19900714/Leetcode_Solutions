
# Space: O(n)
# Time: O(n)

# BFS Approach

class Solution:
    def canReach(self, arr, start):
        length = len(arr)
        if length == 1 and start == 0: return True
        visited = set()
        queue = [start]

        while queue:
            cur = queue.pop(0)
            if cur in visited: continue
            if queue[cur] == 0: return True
            visited.add(cur)
            if 0 <= cur + queue[cur] < length: queue.append(cur + queue[cur])
            if 0 <= cur - queue[cur] < length: queue.append(cur - queue[cur])

        return False




