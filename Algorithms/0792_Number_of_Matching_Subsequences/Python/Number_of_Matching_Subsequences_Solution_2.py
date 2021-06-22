
# Space: O(n)
# Time: O(n)

import collections


class Solution:
    def numMatchingSubseq(self, s, words):
        res = 0
        self.cache = collections.defaultdict(list)
        self.result = {}
        for i in range(len(s)):
            self.cache[s[i]].append(i)
        for word in words:
            if word in self.result:
                res += self.result[word]
            else:
                if self.is_subsequence(word):
                    res += 1
        return res

    def is_subsequence(self, s):
        cur_index = -1
        for i in range(len(s)):
            if s[i] not in self.cache: return False
            temp = self.cache[s[i]]
            for j in temp:
                if j > cur_index:
                    cur_index = j
                    break
            else:
                self.result[s] = 0
                return False
        self.result[s] = 1
        return True





