
# Space: O(nlogn)
# Time: O(nlogn)

class Solution:
    def findLongestWord(self, s, d):
        d = sorted(d, key=lambda x: (-len(x), x))
        res = ''

        for word in d:
            index_s, index_word = 0, 0
            while index_s < len(s) and index_word < len(word):
                if s[index_s] == word[index_word]:
                    index_s += 1
                    index_word += 1
                else:
                    index_s += 1

            if index_word == len(word):
                if len(res) > 0 and len(word) < len(res):
                    return res
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res) and word < res:
                    res = word

        return res




