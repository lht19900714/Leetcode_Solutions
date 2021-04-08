
# Space: O(n)
# Time: O(n)

class Solution:
    def totalNQueens(self, n):
        self.queen_position = set()
        self.res = 0

        def backtracking(row_num, queen_count, required_queen, length):
            if queen_count == required_queen:
                self.res += 1
                return

            for x in range(length):
                if self.check_position(x, row_num, length, self.queen_position):
                    self.queen_position.add((row_num, x))
                    backtracking(row_num + 1, queen_count + 1, required_queen, length)
                    self.queen_position.remove((row_num, x))

        backtracking(0, 0, n, n)

        return self.res

    def check_position(self, x, y, length, alist):
        if len(alist) == 0: return True

        for queen_y, queen_x in alist:
            if x == queen_x or y == queen_y: return False

        direction = [[1, 1], [-1, -1], [-1, 1], [1, -1]]

        for dir_y, dir_x in direction:
            temp_x, temp_y = x, y

            while 0 <= temp_x < length and 0 <= temp_y < length:
                if (temp_y, temp_x) in alist: return False
                temp_x += dir_x
                temp_y += dir_y

        return True





