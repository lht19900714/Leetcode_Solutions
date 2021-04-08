
# Space: O(n)
# Time: O(n)

class Solution:
    def __init__(self):
        self.memory_pacific = {}
        self.memory_atlantic = {}

    def pacificAtlantic(self, matrix):
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        res = []
        for y in range(m):
            for x in range(n):
                # print([y,x])
                if self.BFS_pacific(matrix, x, y) and self.BFS_atlantic(matrix, x, y):
                    res.append([y, x])

        return res

    def BFS_pacific(self, matrix, x, y):
        m = len(matrix)
        n = len(matrix[0])
        if y == 0 or x == 0:
            self.memory_pacific[(y, x)] = True
            return True
        if (y, x) in self.memory_pacific:
            return self.memory_pacific[(y, x)]
        queue = [[x, y, matrix[y][x]]]
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        while queue:
            cur_x, cur_y, cur_height = queue.pop(0)
            visited.add((cur_y, cur_x))
            if cur_x == 0 or cur_y == 0:
                self.memory_pacific[(y, x)] = True
                return True
            if (cur_y, cur_x) in self.memory_pacific:
                if self.memory_pacific[(cur_y, cur_x)]:
                    self.memory_pacific[(y, x)] = True
                    return True
                else:
                    continue
            for dir_x, dir_y in direction:
                new_x, new_y = cur_x + dir_x, cur_y + dir_y
                if 0 <= new_x < n and 0 <= new_y < m and (new_y, new_x) not in visited and cur_height >= matrix[new_y][new_x]:
                    queue.append([new_x, new_y, matrix[new_y][new_x]])

        self.memory_pacific[(y, x)] = False

        return False

    def BFS_atlantic(self, matrix, x, y):
        m = len(matrix)
        n = len(matrix[0])
        if y == m - 1 or x == n - 1:
            self.memory_atlantic[(y, x)] = True
            return True
        if (y, x) in self.memory_atlantic:
            return self.memory_atlantic[(y, x)]
        queue = [[x, y, matrix[y][x]]]
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        while queue:
            cur_x, cur_y, cur_height = queue.pop(0)
            visited.add((cur_y, cur_x))
            if cur_x == n - 1 or cur_y == m - 1:
                self.memory_atlantic[(y, x)] = True
                return True
            if (cur_y, cur_x) in self.memory_atlantic:
                if self.memory_atlantic[(cur_y, cur_x)]:
                    self.memory_atlantic[(y, x)] = True
                    return True
                else:
                    continue
            for dir_x, dir_y in direction:
                new_x, new_y = cur_x + dir_x, cur_y + dir_y
                if 0 <= new_x < n and 0 <= new_y < m and (new_y, new_x) not in visited and cur_height >= matrix[new_y][new_x]:
                    queue.append([new_x, new_y, matrix[new_y][new_x]])

        self.memory_atlantic[(y, x)] = False

        return False




                                                                                                                                   