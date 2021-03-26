
# Space: O(n)
# Time: O(n)

class Solution:
    def __init__(self):
        self.memory_pacific = set()
        self.memory_atlantic = set()

    def pacificAtlantic(self, matrix):

        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        res = []
        for y in range(m):
            for x in range(n):
                # print([y,x])
                if self.DFS_pacific(matrix, x, y, matrix[y][x], set()) and self.DFS_atlantic(matrix, x, y, matrix[y][x], set()):
                    res.append([y, x])

        return res

    def DFS_pacific(self, matrix, x, y, height, visited):
        m = len(matrix)
        n = len(matrix[0])
        if not (0 <= x < n and 0 <= y < m): return False
        if matrix[y][x] > height: return False
        if (y, x) in self.memory_pacific: return True
        if (y, x) in visited: return False
        if y == 0 or x == 0:
            self.memory_pacific.add((y, x))
            return True
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dir_x, dir_y in direction:
            visited.add((y, x))
            res = self.DFS_pacific(matrix, x + dir_x, y + dir_y, matrix[y][x], visited)
            visited.remove((y, x))
            if res:
                return True

        return False

    def DFS_atlantic(self, matrix, x, y, height, visited):
        m = len(matrix)
        n = len(matrix[0])
        if not (0 <= x < n and 0 <= y < m): return False
        if matrix[y][x] > height: return False
        if (y, x) in self.memory_atlantic: return True
        if (y, x) in visited: return False
        if y == m - 1 or x == n - 1:
            self.memory_atlantic.add((y, x))
            return True
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dir_x, dir_y in direction:
            visited.add((y, x))
            res = self.DFS_atlantic(matrix, x + dir_x, y + dir_y, matrix[y][x], visited)
            visited.remove((y, x))
            if res:
                return True

        return False





