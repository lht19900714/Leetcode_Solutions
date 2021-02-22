
# Space: O(n)
# Time: O(n)

class Solution:
    def findLongestWord(self, s, d):

        def issubsequence(target, string):
            index_target, index_string = 0, 0
            while index_target < len(target) and index_string < len(string):
                if target[index_target] == string[index_string]:
                    index_target += 1
                    index_string += 1
                else:
                    index_string += 1
            return True if index_target == len(target) else False

        res = ''
        for word in d:
            if issubsequence(word, s):
                res = word if len(word) > len(res) else res
                res = word if len(word) == len(res) and word<res else res

        return res




