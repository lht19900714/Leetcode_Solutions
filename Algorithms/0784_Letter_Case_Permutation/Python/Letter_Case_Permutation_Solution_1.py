
# Space: O(n)
# Time: O(n)


class Solution:
    def letterCasePermutation(self, S):
        if S.isnumeric(): return [S]
        self.res = []

        def dfs(string, cur_index, res):
            if cur_index == len(string):
                self.res.append(res)
                return

            if string[cur_index].isnumeric():
                res += string[cur_index]
                dfs(string, cur_index + 1, res)

            if string[cur_index].isalpha():
                for char in [string[cur_index].lower(), string[cur_index].upper()]:
                    res += char
                    dfs(string, cur_index + 1, res)
                    res = res[:cur_index]

        dfs(S, 0, '')
        return self.res




