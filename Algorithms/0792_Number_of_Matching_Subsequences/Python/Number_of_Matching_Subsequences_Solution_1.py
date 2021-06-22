
# Space: O(n)
# Time: O(n)

class Solution:
    def numMatchingSubseq(self, s, words):
        res = 0
        self.result = {}

        for word in words:
            if word in self.result:
                res += self.result[word]
            else:
                if self.is_subsequence(s, word):
                    res += 1
        return res

    def is_subsequence(self, target, s):
        length1 = len(target)
        length2 = len(s)
        index1, index2 = 0, 0
        while index1 < length1 and index2 < length2:
            if target[index1] == s[index2]: index2 += 1
            if index2 == length2:
                self.result[s] = 1
                return True
            index1 += 1
        self.result[s] = 0
        return False





