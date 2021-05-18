
# Space: O(n)
# Time: O(n)

class Solution:
    def longestStrChain(self, words):
        length = len(words)
        if length == 1: return 1
        cache = {}
        words = sorted(words, key=lambda x: len(x))
        res = 1

        for word in words:
            cache[word] = 1
            word_length = len(word)
            if word_length == 1: continue
            for i in range(word_length):
                temp_word = word[:i] + word[i + 1:]
                if temp_word in cache:
                    cache[word] = max(cache[word], cache[temp_word] + 1)
                    res = max(res,cache[word])

        return res




