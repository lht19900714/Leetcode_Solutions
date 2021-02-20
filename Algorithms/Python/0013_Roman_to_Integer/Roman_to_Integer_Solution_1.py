
# Space: O(1)
# Time: O(n)

class Solution:
    def romanToInt(self, s):
        cache = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0

        for i in range(len(s) - 1):
            if cache[s[i]] < cache[s[i + 1]]:
                res -= cache[s[i]]
            else:
                res += cache[s[i]]

        res += cache[s[-1]]

        return res





                                                                                                                     