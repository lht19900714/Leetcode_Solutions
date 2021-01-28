
# Space: O(n)
# Time: O(n)

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        char_cache = {i + 1: chr(97 + i) for i in range(26)}
        if n == 1: return char_cache[k]

        res = [None for _ in range(n)]

        for i in range(n - 1, -1, -1):
            if k > (i + 1):
                temp_res = k - i
                if temp_res <= 26:
                    res[i] = char_cache[temp_res]
                    k -= temp_res
                else:
                    res[i] = char_cache[26]
                    k -= 26
            elif k == (i + 1):
                res[i] = char_cache[1]
                k -= 1
        return ''.join(res)





