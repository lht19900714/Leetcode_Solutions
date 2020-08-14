
# Space: O(n)
# Time: O(n!)

# same approach as solution 1, improve space complexity

class Solution:
    def combine(self, n: int, k: int):
        if k > n: return []

        def dfs(num, index, temp_res, res, k):
            if len(temp_res) == k:
                res.append(temp_res[:])
                return
            for i in range(index, num + 1):
                temp_res.append(i)
                dfs(num, i + 1, temp_res, res, k)
                temp_res.pop()
            return res

        return dfs(n,1,[],[],k)





