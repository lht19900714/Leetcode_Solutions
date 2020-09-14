# Space: O(n)
# Time: O(n)


class Solution:
    def combinationSum3(self, k, n):
        if k == 1 and n <= 9: return [[n]]
        self.res = []

        def backtracking(start, end, n, k, res, temp_res):
            if res == n and len(temp_res) == k:
                self.res.append(temp_res[:])
                return

            if res >= n or len(temp_res) >= k: return

            for num in range(start, end):
                if num > n: continue
                temp_res.append(num)
                res += num
                backtracking(num + 1, end, n, k, res, temp_res)
                res -= num
                temp_res.pop()

        backtracking(1, 10, n, k, 0, [])
        return self.res





