
# Space: O(n)
# Time: O(n)

class Solution:
    def minimumLengthEncoding(self, words):
        length = len(words)
        if length == 1: return len(words[0]) + 1

        temp = set(words)

        for word in words:
            for i in range(1, len(word)):
                if word[i:] in temp:
                    temp.remove(word[i:])

        return sum(len(word) + 1 for word in temp)




