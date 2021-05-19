
# Space: O(n)
# Time: O(n)

class Solution:
    def longestStrChain(self, words):
        length = len(words)
        if length == 1: return 1
        self.cache = {}

        def dfs(word, words):
            if word in self.cache: return self.cache[word]
            if len(word) == 1:
                self.cache[word] = 1
                return 1
            if len(word) == 0: return 0
            res = 1
            for i in range(len(word)):
                temp = word[:i] + word[i + 1:]
                if temp in words:
                    res = max(res, dfs(temp,words) + 1)
            self.cache[word] = res
            return res

        res = 0
        for word in words:
            res = max(res, dfs(word, words))

        return res




