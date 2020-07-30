
# Space: O(n)
# Time: O(n)

class Solution:
    def wordBreak(self, s, wordDict):
        self.memory = {}
        wordDict = set(wordDict)  # convert list to set to improve execution time

        def recursive_search(string, wordDict):
            if string in self.memory:
                return self.memory[string]
            if string in wordDict:
                self.memory[string] = True
                return True

            for i in range(1, len(string)):  # split string to two parts
                left = string[:i]
                right = string[i:]
                if left in wordDict and recursive_search(right, wordDict):
                    self.memory[string] = True
                    return True
            self.memory[string] = False
            return False

        return recursive_search(s,wordDict)



