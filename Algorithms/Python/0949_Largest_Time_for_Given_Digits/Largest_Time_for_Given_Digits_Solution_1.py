
# Space: O(n)
# Time: O(n)

class Solution:
    def largestTimeFromDigits(self, A):
        permutation = self.permutation(A)
        res = ''
        max_time = -1
        for h1, h2, m1, m2 in permutation:
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if hour < 24 and minute < 60 and hour * 60 + minute >= max_time:
                max_time = hour * 60 + minute
                res = f'{h1}{h2}:{m1}{m2}'
        return res

    def permutation(self, alist):
        length = len(alist)
        self.visited = [0] * length

        def helper(alist, length, temp_res, res):
            if len(temp_res) == length:
                res.append(temp_res[:])
                return
            for i in range(length):
                if self.visited[i] != 0: continue
                self.visited[i] = 1
                temp_res.append(alist[i])
                helper(alist, length, temp_res, res)
                temp_res.pop()
                self.visited[i] = 0
            return res

        return helper(alist, length, [], [])







