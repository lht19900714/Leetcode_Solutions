
# Space: O(n)
# Time: O(2^n)


class Solution:
    def maxLength(self, arr):
        length = len(arr)
        if length == 1: return len(arr[0])
        self.cache = {chr(i): 1 for i in range(97, 97 + 26)}
        self.flag, self.temp_count, self.res = False, 0, 0

        def bfs(arr, temp_res, cur_index):
            self.res = max(self.res, self.temp_count)

            for i in range(cur_index, len(arr)):
                for c in arr[i]:
                    self.cache[c] -= 1
                    if self.cache[c] < 0: self.flag = True
                if not self.flag:
                    self.temp_count += len(arr[i])
                    bfs(arr, temp_res, i + 1)
                    self.temp_count -= len(arr[i])
                for c in arr[i]:
                    self.cache[c] += 1
                self.flag = False

        bfs(arr, 0, 0)
        return self.res





