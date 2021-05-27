
# Space: O(n)
# Time: O(n^2)

class Solution:
    def maxProduct(self, words):
        res = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(set(words[i]).intersection(set(words[j]))) == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res




