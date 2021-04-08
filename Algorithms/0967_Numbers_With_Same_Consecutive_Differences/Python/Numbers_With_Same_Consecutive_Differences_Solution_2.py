# Space: O(n)
# Time: O(n)

# DFS/Backtracking solution

class Solution:
    def numsSameConsecDiff(self, N, K):

        self.data = [i for i in range(10)]

        def dfs(length, K, temp_res, res):
            if len(temp_res) == length:
                res.add(temp_res)
                return

            for num in self.data:
                if num == 0 and len(temp_res)==0 and length > 1: continue # handle leading 0 situation

                if len(temp_res) == 0:
                    temp_res += str(num)
                    dfs(length, K, temp_res, res)
                    temp_res = temp_res[:-1]

                else:
                    if int(temp_res[-1]) - num == K:
                        temp_res += str(num)
                        dfs(length, K, temp_res, res)
                        temp_res = temp_res[:-1]

                    if num - int(temp_res[-1]) == K:
                        temp_res += str(num)
                        dfs(length, K, temp_res, res)
                        temp_res = temp_res[:-1]

            return res

        return dfs(N,K,'',set())




