
# Space: O(1)
# Time: O(n^2)

class Solution:
    def scoreOfParentheses(self, S):
        if len(S) == 2: return 1

        def dfs(string, start, end):
            res, balance = 0, 0
            index = start
            while start <= index < end:
                balance += 1 if string[index] == '(' else -1
                if balance == 0:
                    if index - start == 1:
                        res += 1
                    else:
                        res += 2 * dfs(string, start + 1, index)
                    start = index + 1
                    index = start
                else:
                    index += 1
            return res

        return dfs(S, 0, len(S))




