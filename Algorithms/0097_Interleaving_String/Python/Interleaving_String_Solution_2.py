
# Space: O(n)
# Time: O(n)

class Solution:
    def isInterleave(self, s1, s2, s3):
        length_1, length_2, length_3 = len(s1), len(s2), len(s3)
        if length_1 == length_2 == length_3 == 0: return True
        if length_1 + length_2 != length_3: return False

        s1 = '#' + s1
        s2 = '#' + s2
        s3 = '#' + s3

        dp = [[False for _ in range(length_1 + 1)] for _ in range(length_2 + 1)]

        for y in range(len(dp)):
            for x in range(len(dp[0])):
                if x == 0 and y == 0:
                    dp[y][x] = True
                elif y == 0 and s1[x] == s3[y + x] and dp[y][x - 1] is True:
                    dp[y][x] = True
                elif x == 0 and s2[y] == s3[y + x] and dp[y - 1][x] is True:
                    dp[y][x] = True
                elif s1[x] == s3[y + x] and dp[y][x - 1] is True:
                    dp[y][x] = True
                elif s2[y] == s3[y + x] and dp[y - 1][x] is True:
                    dp[y][x] = True
        return dp[-1][-1]




