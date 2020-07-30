
# Space: O(n)
# Time: O(n)

class Solution:
    def wordBreak(self, s, wordDict):
        self.memory = {}
        wordDict = set(wordDict)  # convert list to set to improve execution time

        def recursive_search(string, wordDict):
            res = []
            if string in self.memory:
                return self.memory[string]
            if string in wordDict:
                res.append(string)

            for i in range(1, len(string)):  # split string to two parts
                left = string[:i]
                right = string[i:]

                if right not in wordDict: continue

                left_res = recursive_search(left, wordDict)
                for each_left_res in left_res:
                    res.append(each_left_res + ' ' + right)

            self.memory[string] = res
            return self.memory[string]

        return recursive_search(s, wordDict)


