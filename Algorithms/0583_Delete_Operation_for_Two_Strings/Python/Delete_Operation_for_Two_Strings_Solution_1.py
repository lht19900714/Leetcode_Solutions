
# Space: O(n)
# Time: O(n)

class Solution:
    def minDistance(self, word1, word2):
        length1, length2 = len(word1), len(word2)
        if length1 == length2 == 0: return 0
        if word1 == word2: return 0

        board = [[0 for _ in range(length1 + 1)] for _ in range(length2 + 1)]
        for y in range(length2 + 1):
            for x in range(length1 + 1):
                if x == 0 or y == 0: continue
                if word1[x - 1] == word2[y - 1]:
                    board[y][x] = board[y - 1][x - 1] + 1
                else:
                    board[y][x] = max(board[y - 1][x], board[y][x - 1])
        res = board[-1][-1]

        return length1 - res + length2 - res





