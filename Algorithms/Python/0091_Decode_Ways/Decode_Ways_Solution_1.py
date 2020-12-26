
# Space: O(n)
# Time: O(n)

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0: return 0
        self.cache = {}
        self.cache[''] = 1

        def recursive(string):
            if string in self.cache: return self.cache[string]
            if string[0] == '0': return 0
            if len(string) == 1: return 1

            temp_res = recursive(string[1:])
            prefix = int(string[:2])

            if 0 < prefix <= 26:
                temp_res += recursive(string[2:])

            self.cache[string] = temp_res

            return temp_res

        return recursive(s)





