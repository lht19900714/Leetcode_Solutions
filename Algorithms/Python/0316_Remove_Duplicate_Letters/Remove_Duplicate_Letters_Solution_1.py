
# Space: O(n)
# Time: O(n)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 1: return s

        data = {char: index for index, char in enumerate(s)}
        visited = {key: 0 for key in data}

        res = []

        for index, char in enumerate(s):
            if visited[char] == 1:
                continue

            if not res or res[-1] < char:
                res.append(char)
                visited[char] = 1

            elif res[-1] > char:

                while res and res[-1] > char and data[res[-1]] > index:
                    visited[res[-1]] = 0
                    res.pop()

                res.append(char)
                visited[char] = 1

        return ''.join(res)





