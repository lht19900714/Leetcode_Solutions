
# Space: O(n)
# Time: O(n!)


class Solution:
    def combine(self, n: int, k: int):
        if k > n: return []

        data = [i for i in range(1, n + 1)]  # list all numbers
        status = [False for _ in range(len(data))]  # identify if current item has been used or not

        def dfs(data, index, temp_res, res, k):
            if len(temp_res) == k:
                res.append(temp_res[:])
                return

            for i in range(index, len(data)):
                if status[i]: continue  # if current number has been used, then pass to next one
                status[i] = True
                temp_res.append(data[i])
                dfs(data, i, temp_res, res, k)
                temp_res.pop()
                status[i] = False
            return res

        return dfs(data, 0, [], [], k)


