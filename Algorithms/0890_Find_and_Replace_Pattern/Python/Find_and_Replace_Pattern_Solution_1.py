
# Space: O(n)
# Time: O(n)

class Solution:
    def findAndReplacePattern(self, words, pattern):
        cache = {}
        res = []
        for word in words:
            if len(word) != len(pattern): continue
            temp_cache = {}
            for i in range(len(word)):
                if word[i] not in temp_cache:
                    cache[pattern[i]] = word[i]
                    temp_cache[word[i]] = pattern[i]
                elif word[i] in temp_cache and temp_cache[word[i]] != pattern[i]:
                    break
            else:
                temp = ''.join(cache[c] for c in pattern)
                if temp == word: res.append(word)

        return res





