
# Space: O(n)
# Time: O(n^2)

class Solution:
    def makesquare(self, matchsticks):
        if not matchsticks: return False
        length = sum(matchsticks) // 4
        if sum(matchsticks) / 4 != length: return False

        matchsticks.sort(reverse=True)
        self.cache = [0, 0, 0, 0]

        def dfs(index, alist, target):
            if index == len(alist):
                return self.cache[0] == self.cache[1] == self.cache[2] == target

            for i in range(4):
                if self.cache[i] + alist[index] <= target:
                    self.cache[i] += alist[index]
                    if dfs(index + 1, alist, target): return True
                    self.cache[i] -= alist[index]
            return False

        return dfs(0, matchsticks, length)




