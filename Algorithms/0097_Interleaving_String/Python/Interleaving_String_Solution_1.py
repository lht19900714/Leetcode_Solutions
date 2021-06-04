
# Space: O(n)
# Time: O(n)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        length_1, length_2, length_3 = len(s1), len(s2), len(s3)
        if length_1 == length_2 == length_3 == 0: return True
        if length_1 + length_2 != length_3: return False

        cache = [[None for _ in range(length_1)] for _ in range(length_2)]

        def dfs(board, s1, s2, s3, index1, index2, index3):
            if index1 == len(s1): return s2[index2:] == s3[index3:]
            if index2 == len(s2): return s1[index1:] == s3[index3:]
            if board[index2][index1] is not None: return board[index2][index1]

            ans = False
            if s1[index1] == s3[index3] and dfs(board, s1, s2, s3, index1 + 1, index2, index3 + 1):
                ans = True
            if s2[index2] == s3[index3] and dfs(board, s1, s2, s3, index1, index2 + 1, index3 + 1):
                ans = True

            board[index2][index1] = ans
            return ans

        return dfs(cache, s1, s2, s3, 0, 0, 0)








